// Render film.html to video, frame by frame (deterministic: every frame is render(t)).
//   node scripts/render.mjs                 -> out/dtm_16x9.mp4, out/dtm_9x16.mp4, out/dtm_1x1.mp4
//   node scripts/render.mjs 16x9            -> one format
//   node scripts/render.mjs --stills 1,12,30 [fmt...]  -> PNG stills in out/stills/
import { createRequire } from "node:module";
const { chromium } = createRequire(import.meta.url)("playwright");
import { spawn } from "node:child_process";
import { mkdirSync } from "node:fs";
import { fileURLToPath, pathToFileURL } from "node:url";
import path from "node:path";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const args = process.argv.slice(2);
let stills = null;
const si = args.indexOf("--stills");
if (si >= 0) { stills = args[si + 1].split(",").map(Number); args.splice(si, 2); }
const formats = args.length ? args : ["16x9", "9x16", "1x1"];
const SIZES = { "16x9": [1920, 1080], "9x16": [1080, 1920], "1x1": [1080, 1080] };

async function open(browser, fmt) {
  const [w, h] = SIZES[fmt];
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  const url = pathToFileURL(path.join(root, "film.html")).href + `?f=${fmt}&render=1`;
  await page.goto(url);
  await page.evaluate(() => document.fonts.ready);
  const fonts = await page.evaluate(() => [...document.fonts].filter(f => f.status === "loaded").length);
  return page;
}

async function renderVideo(browser, fmt) {
  const page = await open(browser, fmt);
  const { FPS, DURATION } = await page.evaluate(() => window.FILM);
  const out = path.join(root, "out", `dtm_${fmt}.mp4`);
  const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(FPS), "-c:v", "mjpeg", "-i", "-",
    "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-profile:v", "high",
    "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
    "-movflags", "+faststart", out], { stdio: ["pipe", "inherit", "inherit"] });
  const done = new Promise((res, rej) => ff.on("close", c => c === 0 ? res() : rej(new Error("ffmpeg " + c))));
  const N = FPS * DURATION;
  for (let i = 0; i < N; i++) {
    await page.evaluate(t => window.render(t), i / FPS);
    const buf = await page.screenshot({ type: "jpeg", quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
    if (i % 300 === 0) console.log(`${fmt}: frame ${i}/${N}`);
  }
  ff.stdin.end();
  await done;
  console.log("wrote", out);
  await page.close();
}

const browser = await chromium.launch();
if (stills) {
  mkdirSync(path.join(root, "out", "stills"), { recursive: true });
  for (const fmt of formats) {
    const page = await open(browser, fmt);
    for (const t of stills) {
      await page.evaluate(t => window.render(t), t);
      await page.screenshot({ path: path.join(root, "out", "stills", `${fmt}_${String(t).padStart(5, "0")}.png`) });
    }
    await page.close();
  }
} else {
  await Promise.all(formats.map(f => renderVideo(browser, f)));
}
await browser.close();
