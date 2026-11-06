# Genererar undersidor och designs.html. Kör: python3 tools/build.py
import os, html
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEL, MOB, MAIL = "031-60 01 62", "070-914 97 18", "kontakt@avloppfav.se"
ADR = "Ryk 255, 446 92 Skepplanda"

SERVICES = [
 dict(slug="avloppsfilmning", name="Avloppsfilmning", img="filmning.jpg",
  lead="Med kamerainspektion av avloppsledningar går det att identifiera stopp, skador och andra problem i rörsystemet.",
  body=["En kamera förs in i ledningen och visar ledningens insida på skärm. Det gör det möjligt att se var ett problem sitter och vad det beror på – utan att gräva.",
        "Filmningen ger ett underlag för att bedöma om ledningen behöver spolas, renoveras eller bytas, och är ofta ett bra första steg vid köp eller renovering av fastighet."],
  when=["Återkommande stopp eller långsam avrinning","Dålig lukt från golvbrunnar eller avlopp","Inför husköp eller renovering","Efter spolning, för att kontrollera resultatet","När ledningarnas ålder eller skick är okänt"]),
 dict(slug="avloppsspolning", name="Avloppsspolning", img="spolning.jpg",
  lead="Spolning av avloppsledningar för att avlägsna avlagringar, smuts och hinder som påverkar avloppssystemets funktion.",
  body=["Med högtrycksspolning löses avlagringar, fett och andra hinder upp och spolas bort ur ledningen.",
        "Spolning kan göras akut vid stopp eller förebyggande som en del av regelbundet underhåll."],
  when=["Stopp i avloppet","Långsam avrinning","Kluckande ljud från avlopp","Förebyggande underhåll","Inför filmning av ledning"]),
 dict(slug="avloppsrenovering", name="Avloppsrenovering", img="arbete-ledningar.jpg",
  lead="Vi utför renovering av befintliga avloppssystem.",
  body=["När avloppsledningar har skador eller slitage kan renovering vara ett alternativ till byte.",
        "Vilken metod som passar beror på ledningarnas skick, dimension och placering. Ofta görs en filmning först för att bedöma förutsättningarna."],
  when=["Sprickor eller skador i ledningen","Rötter som växt in i ledningen","Äldre ledningar med slitage","Återkommande problem trots spolning"]),
 dict(slug="byte-av-avloppsledningar", name="Byte av avloppsledningar", img="arbete-graevning.jpg",
  lead="När befintliga avloppsledningar inte längre fungerar som de ska kan ett byte vara nödvändigt.",
  body=["Vid byte grävs den gamla ledningen fram och ersätts med en ny.",
        "Vi hjälper dig att planera arbetet utifrån fastighetens förutsättningar, från undersökning till färdig ledning."],
  when=["Kollapsade eller kraftigt skadade ledningar","När renovering inte är möjlig","Vid om- eller tillbyggnad","Vid anslutning till ny anläggning"]),
 dict(slug="minireningsverk", name="Minireningsverk", img="biokube.jpg",
  lead="Vi arbetar med anläggning och installation av minireningsverk för enskilda avloppslösningar. Företaget finns listat som återförsäljare hos BioKube.",
  body=["Ett minireningsverk är en anläggning som renar avloppsvatten från exempelvis en fastighet som saknar kommunal avloppsanslutning.",
        "Vi hjälper dig att undersöka förutsättningarna för en lösning som passar din fastighet, och utför installation och relaterade VA-arbeten."],
  when=["Fastighet utan kommunalt avlopp","Byte av gammal avloppsanläggning","Nybyggnation på landsbygden","Begränsad yta för markbädd eller infiltration"]),
 dict(slug="service-och-underhall", name="Service & underhåll", img="service.jpg",
  lead="Regelbunden service och underhåll bidrar till att avloppssystem fungerar som de ska och kan minska risken för kostsamma problem.",
  body=["Genom att kontrollera och underhålla avloppsanläggningen i tid går det ofta att upptäcka problem innan de blir stora.",
        "Vi hjälper till med service av avloppssystem och anläggningar för enskilt avlopp."],
  when=["Löpande service av minireningsverk","Kontroll av befintligt avloppssystem","Förebyggande spolning","Efter ägarbyte av fastighet"]),
 dict(slug="va-teknik", name="VA-teknik", img="arbete-maskiner.jpg",
  lead="Vi erbjuder tjänster inom vatten- och avloppsteknik, inklusive installation, underhåll och åtgärder på befintliga avloppssystem.",
  body=["VA-arbeten omfattar allt från markarbeten och ledningsdragning till installation av anläggningar.",
        "Vi tar hand om arbetet från undersökning till åtgärd."],
  when=["Ledningsdragning för vatten och avlopp","Markarbeten i samband med VA","Åtgärder på befintliga system","Installation av nya anläggningar"]),
]
FAQ = [("Vad kostar det att filma ett avlopp?","Priset beror bland annat på ledningarnas omfattning och förutsättningarna på platsen. Kontakta oss för att beskriva ditt behov och få information om kostnaden."),
("När behöver man spola avloppet?","Avloppsspolning kan vara aktuellt vid återkommande stopp, långsam avrinning eller som en del av förebyggande underhåll."),
("Vad är ett minireningsverk?","Ett minireningsverk är en anläggning som renar avloppsvatten från exempelvis en fastighet som saknar kommunal avloppsanslutning."),
("Kan ni installera enskilt avlopp?","Ja, företaget arbetar med installation av minireningsverk och relaterade arbeten inom vatten och avlopp."),
("Kan ni hjälpa till med gamla avloppsrör?","Ja, företaget arbetar med filmning, renovering och byte av avloppssystem. Vilken åtgärd som är lämplig beror på ledningarnas skick."),
("Vilka områden arbetar ni i?","Vi har vår bas i Skepplanda i Västra Götaland. Kontakta oss för att kontrollera om vi kan hjälpa dig på din ort.")]
STEPS = [("Kontakta oss","Berätta om ditt avloppssystem, din fastighet och vad du behöver hjälp med."),
("Vi går igenom behovet","Vi diskuterar förutsättningarna och bedömer vilka åtgärder eller undersökningar som kan vara aktuella."),
("Förslag på lösning","Du får information om lämpliga åtgärder och möjlighet att diskutera ett upplägg för arbetet."),
("Genomförande","Vi utför det överenskomna arbetet med fokus på funktion och ett väl genomfört resultat.")]
WHY = [("Brett tjänsteutbud","Från filmning och spolning till renovering och installation av kompletta avloppslösningar."),
("Anpassade lösningar","Varje fastighet har sina egna förutsättningar. Därför utgår arbetet från anläggningens behov."),
("Från undersökning till åtgärd","Vi arbetar med både felsökning, installation och underhåll av avloppssystem."),
("Lokal förankring","Med bas i Skepplanda erbjuder vi tjänster inom vatten och avlopp i Västsverige.")]

def head(title, desc, base, extra=""):
    return f'''<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;800&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}style.css"><link rel="stylesheet" href="{base}pages.css">{extra}</head><body>'''

def header(base, solid=True):
    return f'''<header class="site-header{' solid always' if solid else ''}" id="header">
<a class="logo" href="{base}index.html"><img src="{base}assets/logo-transparent.png" alt="" width="36" height="36"><span>Avloppsteknik Väst</span></a>
<nav class="nav" id="nav"><div class="dd"><a href="{base}tjanster.html">Tjänster ▾</a><div class="dd-menu">{''.join(f'<a href="{base}tjanster/{s["slug"]}.html">{s["name"]}</a>' for s in SERVICES)}</div></div>
<a href="{base}om-oss.html">Om oss</a><a href="{base}minireningsverk.html">Minireningsverk</a><a href="{base}vanliga-fragor.html">Frågor</a><a href="{base}kontakt.html" class="btn btn-sm">Kontakt</a></nav>
<button class="burger" id="burger" aria-label="Meny">☰</button></header>'''

def footer(base):
    return f'''<footer class="footer"><div><strong>Fastighet &amp; Avloppsteknik Väst AB</strong><p>Avloppsteknik, VA-installationer och avloppsrening med bas i Skepplanda, Västra Götaland.</p><p>Org.nr 559368-4011</p></div>
<div><h4>Tjänster</h4>{''.join(f'<a href="{base}tjanster/{s["slug"]}.html">{s["name"]}</a>' for s in SERVICES)}</div>
<div><h4>Kontakt</h4><p>Andreas Landström</p><a href="tel:+4631600162">Tel {TEL}</a><a href="tel:+46709149718">Mobil {MOB}</a><a href="mailto:{MAIL}">{MAIL}</a><p>{ADR}</p></div>
<p class="fine">© 2026 Fastighet &amp; Avloppsteknik Väst AB · Webbplats av Elevate Studio</p></footer>
<script src="{base}script.js"></script></body></html>'''

def pagehero(base, eyebrow, title, lead, img, crumbs):
    c = ' / '.join(f'<a href="{base}{u}">{n}</a>' if u else n for n,u in crumbs)
    return f'''<section class="page-hero" style="background-image:linear-gradient(90deg,#0b1f33f2,#0b1f3399 55%,#0b1f3340),url('{base}assets/{img}')"><div class="page-hero-in">
<nav class="crumbs">{c}</nav><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p class="lead">{lead}</p>
<div class="hero-cta"><a href="{base}kontakt.html" class="btn btn-lg">Begär offert →</a><a href="tel:+4631600162" class="btn btn-ghost btn-lg">Ring {TEL}</a></div></div></section>'''

def cta(base):
    return f'''<section class="cta-band"><div><h2>Behöver du hjälp med ditt avlopp?</h2><p>Beskriv ditt ärende så återkommer vi.</p></div>
<div class="hero-cta"><a href="{base}kontakt.html" class="btn btn-lg">Skicka förfrågan</a><a href="tel:+46709149718" class="btn btn-outline-light btn-lg">{MOB}</a></div></section>'''

def faq_html(items):
    return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)

def steps_html():
    return '<ol class="steps">' + ''.join(f'<li class="reveal"><span>0{i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i,(t,d) in enumerate(STEPS)) + '</ol>'

def form_html(selected=""):
    opts = ''.join(f'<option{" selected" if s["name"]==selected else ""}>{s["name"]}</option>' for s in SERVICES) + '<option>Övrigt</option>'
    return f'''<form class="form" action="mailto:{MAIL}" method="post" enctype="text/plain">
<label>Namn<input name="Namn" required></label><label>Telefonnummer<input name="Telefon" type="tel"></label>
<label>E-postadress<input name="E-post" type="email" required></label><label>Typ av tjänst<select name="Tjänst"><option value="">Välj tjänst</option>{opts}</select></label>
<label class="full">Ort<input name="Ort"></label><label class="full">Beskrivning av ärendet<textarea name="Beskrivning" rows="5"></textarea></label>
<button class="btn full" type="submit">Skicka förfrågan</button></form>'''

def w(path, s):
    p = os.path.join(R, path); os.makedirs(os.path.dirname(p), exist_ok=True); open(p,'w').write(s)

# --- Tjänstesidor
for i,s in enumerate(SERVICES):
    b = "../"
    others = [o for o in SERVICES if o is not s]
    rel = [f for f in FAQ if any(k in f[0].lower() for k in s["name"].lower().split()[:1])] or FAQ[:3]
    w(f"tjanster/{s['slug']}.html", head(f"{s['name']} – Fastighet & Avloppsteknik Väst AB", s["lead"], b) + header(b) +
      pagehero(b, "Tjänst", s["name"], s["lead"], s["img"], [("Start","index.html"),("Tjänster","tjanster.html"),(s["name"],None)]) +
      f'''<section class="svc"><article class="svc-main reveal"><h2>Om {s["name"].lower()}</h2>{''.join(f"<p>{p}</p>" for p in s["body"])}
<h3>När kan det vara aktuellt?</h3><ul class="checks">{''.join(f"<li>{x}</li>" for x in s["when"])}</ul></article>
<aside class="svc-side reveal"><div class="side-card"><h3>Kontakta oss</h3><p>Andreas Landström</p><a class="big" href="tel:+4631600162">{TEL}</a><a href="tel:+46709149718">Mobil {MOB}</a><a href="mailto:{MAIL}">{MAIL}</a><a href="{b}kontakt.html" class="btn full">Begär offert</a></div>
<div class="side-card light"><h3>Övriga tjänster</h3>{''.join(f'<a href="{o["slug"]}.html">{o["name"]} →</a>' for o in others)}</div></aside></section>
<section class="section"><p class="eyebrow">Arbetsgång</p><h2>Så går det till</h2>{steps_html()}</section>
<section class="section faq"><h2>Vanliga frågor</h2>{faq_html(rel)}</section>''' + cta(b) + footer(b))

# --- Tjänster översikt
b=""
w("tjanster.html", head("Tjänster – Fastighet & Avloppsteknik Väst AB","Våra tjänster inom vatten och avlopp.",b) + header(b) +
  pagehero(b,"Tjänster","Våra tjänster inom vatten &amp; avlopp","Från inspektion och underhåll till installation och renovering – vi hjälper dig att hitta rätt lösning för ditt avloppssystem.","spolning.jpg",[("Start","index.html"),("Tjänster",None)]) +
  '<section class="section"><div class="svc-list">' + ''.join(f'''<a class="svc-row reveal" href="tjanster/{s["slug"]}.html"><img src="assets/{s["img"]}" alt=""><div><span>0{i+1}</span><h2>{s["name"]}</h2><p>{s["lead"]}</p><em>Läs mer →</em></div></a>''' for i,s in enumerate(SERVICES)) + '</div></section>' + cta(b) + footer(b))

# --- Om oss
w("om-oss.html", head("Om oss – Fastighet & Avloppsteknik Väst AB","Avloppsteknik med bas i Skepplanda.",b) + header(b) +
  pagehero(b,"Om oss","Din partner inom avloppsteknik","Fastighet &amp; Avloppsteknik Väst AB arbetar med installation, renovering, inspektion och underhåll av avloppssystem.","arbete-maskiner.jpg",[("Start","index.html"),("Om oss",None)]) +
  f'''<section class="split"><div class="reveal"><h2>Lokalt företag i Skepplanda</h2><p>Fastighet &amp; Avloppsteknik Väst AB är ett företag med bas i Skepplanda som arbetar med installation, renovering, inspektion och underhåll av avloppssystem.</p><p>Vi hjälper fastighetsägare att hitta fungerande lösningar för vatten och avlopp, oavsett om det handlar om att undersöka ett befintligt system eller installera en ny avloppsanläggning.</p></div><img class="reveal" src="assets/arbete-graevning.jpg" alt=""></section>
<section class="why"><p class="eyebrow">Varför välja oss</p><h2>Rätt lösning för ditt avloppssystem</h2><div class="why-grid">{''.join(f'<div class="reveal"><h3>{t}</h3><p>{d}</p></div>' for t,d in WHY)}</div></section>
<section class="section"><div class="facts"><div><span>Bas</span><strong>Skepplanda</strong></div><div><span>Område</span><strong>Västsverige</strong></div><div><span>Återförsäljare</span><strong>BioKube</strong></div><div><span>Kontaktperson</span><strong>Andreas Landström</strong></div></div></section>
<section class="gallery">{''.join(f'<img class="reveal" src="assets/{x}" alt="">' for x in ["arbete-jordkallare.jpg","arbete-ledningar.jpg","filmning.jpg","service.jpg"])}</section>''' + cta(b) + footer(b))

# --- Minireningsverk
w("minireningsverk.html", head("Minireningsverk – Fastighet & Avloppsteknik Väst AB","Installation av minireningsverk. BioKube-återförsäljare.",b) + header(b) +
  pagehero(b,"Minireningsverk · BioKube-återförsäljare","Moderna lösningar för enskilt avlopp","Ett minireningsverk kan vara en effektiv lösning för fastigheter som saknar anslutning till kommunalt avlopp.","biokube.jpg",[("Start","index.html"),("Minireningsverk",None)]) +
  f'''<section class="split"><div class="reveal"><h2>Vad är ett minireningsverk?</h2><p>Ett minireningsverk är en anläggning som renar avloppsvatten från exempelvis en fastighet som saknar kommunal avloppsanslutning.</p><p>Vi arbetar med installation av minireningsverk och relaterade VA-arbeten, och hjälper dig att undersöka förutsättningarna för en lösning som passar din fastighet. Företaget finns listat som återförsäljare hos BioKube.</p></div><img class="reveal" src="assets/arbete-jordkallare.jpg" alt=""></section>
<section class="section"><p class="eyebrow">Passar för</p><h2>När kan ett minireningsverk vara rätt val?</h2><ul class="checks cols">{''.join(f"<li>{x}</li>" for x in SERVICES[4]["when"])}</ul></section>
<section class="section"><p class="eyebrow">Från förfrågan till färdig anläggning</p><h2>Så går det till</h2>{steps_html()}</section>
<section class="section faq"><h2>Vanliga frågor</h2>{faq_html([FAQ[2],FAQ[3],FAQ[5]])}</section>''' + cta(b) + footer(b))

# --- FAQ
w("vanliga-fragor.html", head("Vanliga frågor – Fastighet & Avloppsteknik Väst AB","Svar på vanliga frågor om avlopp.",b) + header(b) +
  pagehero(b,"Vanliga frågor","Frågor om avlopp","Hittar du inte svaret? Ring eller skicka en förfrågan.","filmning.jpg",[("Start","index.html"),("Vanliga frågor",None)]) +
  f'<section class="section faq">{faq_html(FAQ)}</section>' + cta(b) + footer(b))

# --- Kontakt
w("kontakt.html", head("Kontakt – Fastighet & Avloppsteknik Väst AB","Kontakta oss om avlopp.",b) + header(b) +
  pagehero(b,"Kontakt","Behöver du hjälp med ditt avlopp?","Oavsett om du behöver undersöka ett avloppssystem, åtgärda ett problem eller installera en ny anläggning är du välkommen att kontakta oss.","service.jpg",[("Start","index.html"),("Kontakt",None)]) +
  f'''<section class="contact"><div class="reveal"><dl><dt>Telefon</dt><dd><a href="tel:+4631600162">{TEL}</a></dd><dt>Mobil</dt><dd><a href="tel:+46709149718">{MOB}</a></dd><dt>E-post</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd><dt>Adress</dt><dd>{ADR}</dd><dt>Kontaktperson</dt><dd>Andreas Landström</dd><dt>Org.nr</dt><dd>559368-4011</dd></dl>
<iframe class="map" title="Karta Skepplanda" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=12.00%2C57.95%2C12.12%2C58.00&amp;layer=mapnik"></iframe></div><div class="reveal">{form_html()}</div></section>''' + footer(b))
print("pages ok")
