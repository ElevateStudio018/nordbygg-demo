# Efterbearbetning för PageSpeed: inline-CSS, självhostade typsnitt, webp, lazy-video.
# Idempotent. Kör efter build.py:  python3 tools/optimize.py
import os, re, glob
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = {'arbete-graevning':(1200,1600),'arbete-jordkallare':(1200,1600),'arbete-ledningar':(1200,1600),'arbete-maskiner':(960,720),
       'biokube':(1600,1200),'filmning':(1200,798),'service':(1200,800),'spolning':(1200,1812)}

def mincss(c):
    c = re.sub(r'/\*.*?\*/', '', c, flags=re.S)
    c = re.sub(r'\s+', ' ', c)
    c = re.sub(r'\s*([{};:,>])\s*', r'\1', c)
    return c.replace(';}', '}').strip()

def css_for(base):
    fonts = (f"@font-face{{font-family:Inter;font-style:normal;font-weight:400 600;font-display:swap;src:url({base}assets/fonts/inter.woff2) format('woff2')}}"
             f"@font-face{{font-family:Manrope;font-style:normal;font-weight:600 800;font-display:swap;src:url({base}assets/fonts/manrope.woff2) format('woff2')}}")
    c = open(os.path.join(R,'style.css')).read() + open(os.path.join(R,'pages.css')).read()
    return fonts + mincss(c)

def srcset(name, base):
    w,h = IMG[name]
    return f'src="{base}assets/img/{name}-960.webp" srcset="{base}assets/img/{name}-480.webp 480w, {base}assets/img/{name}-720.webp 720w, {base}assets/img/{name}-960.webp 960w" sizes="(max-width:700px) 92vw, (max-width:1100px) 45vw, 400px" width="{w}" height="{h}"'

def process(path):
    base = '../' if os.sep+'tjanster'+os.sep in path else ''
    s = open(path).read()
    if 'designs.html' in path: return
    # 1. CSS + typsnitt inline
    s = re.sub(r'<link rel="preconnect" href="https://fonts.googleapis.com">\s*', '', s)
    s = re.sub(r'<link href="https://fonts.googleapis.com/[^"]*" rel="stylesheet">\s*', '', s)
    s = re.sub(r'<link rel="stylesheet" href="(\.\./)?(style|pages)\.css">\s*', '', s)
    s = re.sub(r'<link rel="preload" as="font"[^>]*>|<style id="css">.*?</style>', '', s, flags=re.S)
    s = s.replace('</head>', f'<link rel="preload" as="font" type="font/woff2" href="{base}assets/fonts/inter.woff2" crossorigin><style id="css">{css_for(base)}</style></head>', 1)
    # 2. Bilder -> webp med srcset
    def img(m):
        tag = m.group(0); name = m.group(2)
        if name not in IMG: return tag
        rest = re.sub(r'\s(src|width|height|loading|decoding|srcset|sizes)="[^"]*"', '', tag[4:-1])
        return f'<img {srcset(name, base)} loading="lazy" decoding="async"{rest}>'
    s = re.sub(r'<img [^>]*src="(\.\./)?assets/(?:img/)?([a-z-]+?)(?:-\d+)?\.(?:jpg|webp)"[^>]*>', img, s)
    # bakgrundsbilder
    s = re.sub(r"url\('?(\.\./)?assets/([a-z-]+)\.jpg'?\)", lambda m: f"url({m.group(1) or ''}assets/img/{m.group(2)}-960.webp)" if m.group(2) in IMG else m.group(0), s)
    # 3. Logga
    s = re.sub(r'<img src="(\.\./)?assets/(?:logo-transparent\.png|img/logo\.webp)"[^>]*>',
               lambda m: f'<img src="{m.group(1) or ""}assets/img/logo.webp" alt="Fastighet &amp; Avloppsteknik Väst AB" width="231" height="122">', s)
    # 4. Hero: poster som LCP-bild, videor laddas senare
    if 'id="heroVideos"' in s and 'hero-poster-' not in s:
        s = s.replace('<div class="hero-videos" id="heroVideos">',
          '<div class="hero-videos" id="heroVideos">\n    <img class="hero-media hero-still" src="assets/img/hero-poster-1280.webp" srcset="assets/img/hero-poster-640.webp 640w, assets/img/hero-poster-1280.webp 1280w" sizes="100vw" width="1600" height="900" alt="" fetchpriority="high">')
        s = re.sub(r'<video class="hero-media( on)?"[^>]*>\s*<source src="assets/([a-z0-9-]+)\.mp4" type="video/mp4"></video>',
                   lambda m: f'<video class="hero-media" muted playsinline preload="none" data-src="assets/{m.group(2)}"></video>', s)
    # 5. Formulär utan mailto-action (blandat innehåll)
    s = s.replace('<form class="form" action="mailto:kontakt@avloppfav.se" method="post" enctype="text/plain">', '<form class="form" data-mailto="kontakt@avloppfav.se">')
    # 6. Rubrikordning i footer
    s = re.sub(r'<h4>([^<]*)</h4>', r'<h2 class="ft-h">\1</h2>', s)
    # 8. <main>-landmärke
    if '<main' not in s:
        s = s.replace('</header>', '</header><main id="main">', 1)
        s = s.replace('<footer', '</main><footer', 1)
    # 7. tel-länk med mellanslag
    s = s.replace('tel:+46316001 62', 'tel:+4631600162')
    open(path, 'w').write(s)

for p in glob.glob(os.path.join(R,'*.html')) + glob.glob(os.path.join(R,'tjanster','*.html')):
    process(p)
print('optimerat')
