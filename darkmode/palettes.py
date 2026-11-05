# Dark-mode palettes per design system (DS).
# Each DS: tokens -> dark value. Tokens not listed keep their light value.
# "flip_text": tokens that are dark in light mode and are mostly used as TEXT; in dark mode they become light,
#              and any rule that uses them as a background/border gets pinned to the original value.
# "keep_text": tokens that are light in light mode but used as TEXT on dark bands (e.g. cream on navy):
#              in dark mode the token becomes a dark surface, and rules using it as text get pinned light.

SHADOW = '0 1px 2px rgba(0,0,0,.35),0 6px 18px -6px rgba(0,0,0,.55)'
SHADOW_LG = '0 2px 4px rgba(0,0,0,.35),0 18px 40px -14px rgba(0,0,0,.7)'

DS = {}

# ---------- GeoArcade (home, units, FRQ Exam Prep Room) ----------
DS['ga'] = dict(
    tokens={
        '--paper': '#100D24', '--paper-2': '#181437', '--card': '#1D1945',
        '--ink': '#F2EFFF', '--ink-2': '#CBC5EC', '--ink-3': '#A7A1CF',
        '--line': '#312C5F', '--line-2': '#403A7A',
        '--l1-soft': '#1B2A5E', '--l1-deep': '#A3C0FF',
        '--l2-soft': '#4A2418', '--l2-deep': '#FFA98E',
        '--l3-soft': '#311F62', '--l3-deep': '#C9ADFF',
        '--l4-soft': '#0E3B37', '--l4-deep': '#63D6C9',
        '--sun-soft': '#3F3210', '--mint-soft': '#0E3B37', '--pink-soft': '#4A1A3B',
        '--red-soft': '#4B1D1D', '--green-soft': '#163B25',
        '--green': '#2FBF63', '--red': '#F0605F',
        '--sh': SHADOW, '--sh-lg': SHADOW_LG,
    },
    flip_text=['--ink'],          # --ink is also used as a dark band background in a few rules
    keep_text=[],
    card='var(--card)', paper='var(--paper)', paper_rgb=(16,13,36), ink='var(--ink)', line='var(--line)', soft_bg='var(--paper-2)',
    toggle=dict(bg='#1D1945', fg='#FFC83D', border='#403A7A', font="'Fredoka',system-ui,sans-serif"),
)

# ---------- World Compass (home, units) and its writing tools ----------
DS['wc'] = dict(
    tokens={
        '--bg': '#0E1230', '--bg-2': '#141A3E', '--surface': '#171D47', '--surface-2': '#1F2656', '--paper': '#1A2050',
        '--line': '#2D3572', '--line-2': '#3C458C',
        '--ink': '#EEF0FA', '--ink-2': '#C6CBE8', '--muted': '#A3AACF',
        '--title': '#F1E4B8',
        '--gold-ink': '#E6CB73', '--gold-deep': '#E6CB73', '--gold-soft': '#3A3112',
        '--accent': '#E07C88', '--accent-soft': '#3D1E24', '--asoft': '#3D1E24',
        '--good': '#4CC777', '--good-soft': '#173A24', '--bad': '#F07167', '--bad-soft': '#44201C',
        '--green': '#4CC777', '--green-l': '#173A24', '--green-b': '#2B6A3F',
        '--red': '#F07167', '--red-l': '#44201C', '--red-b': '#7A3530',
        '--yellow': '#F2C94C', '--yellow-l': '#3B3110', '--yellow-b': '#7A6A24',
        '--blue': '#7FB3F0', '--blue-l': '#17304F', '--plum': '#C9A6F0', '--plum-l': '#2F2246',
        '--tT': '#7FB3F0', '--tE': '#F0A36A', '--tA': '#C9A6F0', '--tO': '#4CC777',
        '--shadow': SHADOW, '--shadow-lift': SHADOW_LG,
    },
    # --navy is used as TEXT 37 times and as BG 21 times. Keep the token (bands stay navy) and
    # lighten the text uses instead.
    flip_text=[],
    text_pins={'--navy': '#B9C4FF', '--accent': None, '--green': None, '--red': None, '--plum': None, '--blue': None},
    keep_text=[],
    card='var(--surface)', paper='var(--bg)', paper_rgb=(14,18,48), ink='var(--ink)', line='var(--line)', soft_bg='var(--surface-2)',
    toggle=dict(bg='#171D47', fg='#E3C464', border='#3C458C', font="Arial,Helvetica,sans-serif"),
)

# ---------- Euro Atlas (home, units, periods, -Isms) ----------
DS['ea'] = dict(
    tokens={
        '--paper': '#0F1527', '--cream': '#151D33', '--cream-warm': '#1B243E',
        '--navy-deep': '#0A1020',
        '--brass': '#C9A54F', '--brass-ink': '#E2C782', '--brass-display': '#DDBB6A', '--brass-light': '#E8D394',
        '--ink': '#EDE8DC', '--slate': '#BBC1D1', '--line': '#2E3957',
        '--accent-red': '#E07A7A', '--good': '#7DBF92', '--good-soft': '#173125', '--bad': '#E07A7A', '--bad-soft': '#3A1F22',
        '--lift': SHADOW, '--lift-2': SHADOW_LG, '--hair': '0 1px 0 rgba(255,255,255,.06)',
    },
    flip_text=[],
    # dark tokens used as text on cream: lighten those text uses only
    text_pins={'--navy': '#B9C8F0', '--navy-deep': '#C7D2F2', '--navy-soft': '#A9B9E6', '--forest': '#8CCBA0', '--plum': '#D4A4C6'},
    # --cream is used as text on navy bands: keep those light
    keep_text=['--cream'],
    keep_text_value={'--cream': '#F7F1E5'},
    card='var(--cream)', paper='var(--paper)', paper_rgb=(15,21,39), ink='var(--ink)', line='var(--line)', soft_bg='var(--cream-warm)',
    toggle=dict(bg='#151D33', fg='#D4B05E', border='#2E3957', font="'DM Sans',system-ui,sans-serif"),
)

# ---------- Euro Atlas writing tools (SAQ Sketchbook, LEQ Atelier, DBQ Archive) ----------
DS['eat'] = dict(
    tokens={
        '--paper': '#0F1527', '--paper-2': '#161E36', '--card': '#1B2440',
        '--ink': '#EDE8DC', '--ink-2': '#C4CBDD', '--ink-3': '#A3ACC4',
        '--line': '#2F3A5A', '--line-2': '#3E4B72',
        '--navy-soft': '#223457',
        '--brass': '#C9A54F', '--brass-deep': '#E6CB7A', '--brass-soft': '#3A3014', '--brass-light': '#E8D394',
        '--wine-deep': '#F0A0AE', '--wine-soft': '#3E2229',
        '--forest-deep': '#8CD1A6', '--forest-soft': '#163125',
        '--plum-deep': '#CDB2F2', '--plum-soft': '#2C2247',
        '--sky-deep': '#9CC2F2', '--sky-soft': '#17304F',
        '--gold-soft': '#3B3110', '--red-soft': '#4B1D1D', '--green-soft': '#163125',
        '--sh': SHADOW, '--sh-lg': SHADOW_LG,
    },
    flip_text=[],
    text_pins={'--navy': '#B9C8F0', '--navy-deep': '#C7D2F2', '--forest': '#8CD1A6', '--plum': '#CDB2F2', '--wine': '#F0A0AE', '--brass': '#E6CB7A'},
    keep_text=[],
    card='var(--card)', paper='var(--paper)', paper_rgb=(15,21,39), ink='var(--ink)', line='var(--line)', soft_bg='var(--paper-2)',
    toggle=dict(bg='#1B2440', fg='#D4B05E', border='#3E4B72', font="'DM Sans',system-ui,sans-serif"),
)

# ---------- Chef's DBQ Café ----------
DS['cafe'] = dict(
    tokens={
        '--creme': '#1C1612', '--craie': '#2A221C', '--marbre': '#211A15', '--vein': '#3E342C',
        '--esp': '#F3EAE0', '--esp-2': '#D8CBBE', '--esp-3': '#B5A799',
        '--laiton-d': '#E2BC6E', '--laiton-s': '#3A2E14',
        '--vert': '#7FC094', '--vert-s': '#173125', '--warn': '#F0B35A', '--warn-s': '#3F2F10', '--bad': '#F08A8F', '--bad-s': '#42201F',
    },
    flip_text=[],
    text_pins={'--rouge': '#F08A8F', '--ardoise': '#DDE3DF'},
    keep_text=['--craie'],
    keep_text_value={'--craie': '#ECE7DA'},
    card='var(--marbre)', paper='var(--creme)', paper_rgb=(28,22,18), ink='var(--esp)', line='var(--vein)', soft_bg='var(--craie)',
    toggle=dict(bg='#211A15', fg='#E2BC6E', border='#3E342C', font="'Lexend',system-ui,sans-serif"),
)

# ---------- Lang Studio ----------
DS['lang'] = dict(
    tokens={
        '--ink': '#E9F0EE', '--muted': '#A9BCB8', '--paper': '#0F1A1C', '--white': '#162527',
        '--line': '#2B3E3F', '--soft': '#1C2F2F', '--teal': '#5FC0AE', '--gold': '#E6CC8A',
    },
    flip_text=['--ink'],
    text_pins={},
    keep_text=[],
    card='var(--white)', paper='var(--paper)', paper_rgb=(15,26,28), ink='var(--ink)', line='var(--line)', soft_bg='var(--soft)',
    toggle=dict(bg='#162527', fg='#E6CC8A', border='#2B3E3F', font="system-ui,sans-serif"),
)
