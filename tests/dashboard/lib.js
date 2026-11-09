// Shared paths for the dashboard tests. Made-up sample data only — never put real student data here.
const path = require('path'), fs = require('fs');
const HTML_PATH = path.resolve(__dirname, '../../teacher-dashboard.html');
const OUT = process.env.DASH_OUT || path.resolve(__dirname, 'out');
fs.mkdirSync(OUT, {recursive: true});
module.exports = {HTML_PATH, FILE_URL: 'file://' + HTML_PATH, OUT, FIX: path.resolve(__dirname, 'fixtures')};
