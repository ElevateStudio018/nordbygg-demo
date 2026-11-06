# Bygger designs.html: 5 varianter per sektion att välja mellan.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build import *
A = "assets/"
def lab(sec, k, name): return f'<div class="pick" id="{sec}-{k}"><span>{sec.upper()} {k}</span>{name}</div>'
S = []
def add(sec, k, name, body): S.append(lab(sec,k,name) + body)
cta2 = f'<div class="hero-cta"><a href="kontakt.html" class="btn btn-lg">Begär offert →</a><a href="tjanster.html" class="btn btn-ghost btn-lg">Våra tjänster</a></div>'
vid = f'<video autoplay muted loop playsinline poster="{A}hero-poster.jpg"><source src="{A}hero.mp4" type="video/mp4"></video>'

# ---------- HERO
add("hero","A","Helskärmsvideo, stor rubrik vänster",f'<section class="hA">{vid}<div class="ov"></div><div class="in"><p class="eyebrow">Fastighet &amp; Avloppsteknik Väst AB</p><h1>Vatten &amp; avlopp<br><b>i Västsverige.</b></h1><p>Avloppsfilmning, spolning, renovering och installation av minireningsverk. Från felsökning till färdig lösning.</p>{cta2}</div></section>')
add("hero","B","Delad: text på ljus yta, video till höger",f'<section class="hB"><div class="in"><p class="eyebrow">Skepplanda · Västra Götaland</p><h1>Från felsökning till färdig lösning.</h1><p>Vi hjälper dig med avloppsfilmning, spolning, renovering och installation av minireningsverk.</p>{cta2.replace("btn-ghost","btn-outline")}<div class="meta"><div><b>{TEL}</b><span>Telefon</span></div><div><b>BioKube</b><span>Återförsäljare</span></div></div></div><div class="media">{vid}</div></section>')
add("hero","C","Centrerad, telefonnummer i fokus",f'<section class="hC">{vid}<div class="ov"></div><div class="in"><p class="eyebrow">Vatten &amp; avlopp i Västsverige</p><h1>Problem med avloppet?</h1><p>Ring oss direkt eller skicka en förfrågan.</p><a class="phone" href="tel:+4631600162">{TEL}</a><a href="kontakt.html" class="btn btn-lg">Skicka förfrågan</a></div></section>')
add("hero","D","Inramad video med infolist",f'<section class="hD"><div class="frame">{vid}<div class="ov"></div><div class="in"><h1>Professionella lösningar inom vatten &amp; avlopp</h1>{cta2}</div></div><div class="bar"><div><span>Filmning</span>Kamerainspektion</div><div><span>Spolning</span>Stopp &amp; underhåll</div><div><span>Renovering</span>Befintliga system</div><div><span>Minireningsverk</span>BioKube</div></div></section>')
add("hero","E","Redaktionell: stor typografi + bildkollage",f'<section class="hE"><h1>Avlopp<br>&amp; VA-teknik</h1><div class="row"><p>Fastighet &amp; Avloppsteknik Väst AB arbetar med installation, renovering, inspektion och underhåll av avloppssystem – med bas i Skepplanda.</p>{cta2.replace("btn-ghost","btn-outline")}</div><div class="coll"><img src="{A}arbete-graevning.jpg" alt=""><img src="{A}filmning.jpg" alt=""><img src="{A}biokube.jpg" alt=""></div></section>')

# ---------- TJÄNSTER
sv = SERVICES
add("tjanster","A","Bildkort i rutnät",'<section class="sec"><h2>Våra tjänster</h2><div class="tA">'+''.join(f'<a href="tjanster/{s["slug"]}.html"><img src="{A}{s["img"]}" alt=""><div><h3>{s["name"]}</h3><p>{s["lead"]}</p></div></a>' for s in sv[:6])+'</div></section>')
add("tjanster","B","Numrerad lista, bild visas vid hover",'<section class="sec"><h2>Våra tjänster</h2><div class="tB">'+''.join(f'<a href="tjanster/{s["slug"]}.html"><span>0{i+1}</span><h3>{s["name"]}</h3><p>{s["lead"]}</p><img src="{A}{s["img"]}" alt=""><em>→</em></a>' for i,s in enumerate(sv))+'</div></section>')
add("tjanster","C","Bento-rutnät, olika storlekar",'<section class="sec"><h2>Våra tjänster</h2><div class="tC">'+''.join(f'<a class="c{i}" href="tjanster/{s["slug"]}.html" style="--img:url({A}{s["img"]})"><h3>{s["name"]}</h3><p>{s["lead"]}</p></a>' for i,s in enumerate(sv))+'</div></section>')
add("tjanster","D","Flikar – en tjänst i taget",'<section class="sec"><h2>Våra tjänster</h2><div class="tD">'+''.join(f'<input type="radio" name="td" id="td{i}"{" checked" if i==0 else ""}><label for="td{i}">{s["name"]}</label>' for i,s in enumerate(sv))+''.join(f'<div class="pane"><img src="{A}{s["img"]}" alt=""><div><h3>{s["name"]}</h3><p>{s["lead"]}</p><p>{s["body"][0]}</p><a class="btn" href="tjanster/{s["slug"]}.html">Läs mer</a></div></div>' for s in sv)+'</div></section>')
add("tjanster","E","Mörk sektion, textkolumner med linjer",'<section class="sec dark"><p class="eyebrow">Tjänster</p><h2>Från inspektion till installation</h2><div class="tE">'+''.join(f'<a href="tjanster/{s["slug"]}.html"><h3>{s["name"]}</h3><p>{s["lead"]}</p><em>Läs mer →</em></a>' for s in sv)+'</div></section>')

# ---------- OM OSS
om1="Fastighet &amp; Avloppsteknik Väst AB är ett företag med bas i Skepplanda som arbetar med installation, renovering, inspektion och underhåll av avloppssystem."
om2="Vi hjälper fastighetsägare att hitta fungerande lösningar för vatten och avlopp, oavsett om det handlar om att undersöka ett befintligt system eller installera en ny avloppsanläggning."
add("om","A","Text + bild sida vid sida",f'<section class="oA"><div><p class="eyebrow">Om oss</p><h2>Din partner inom avloppsteknik</h2><p>{om1}</p><p>{om2}</p><a href="om-oss.html" class="btn btn-outline">Mer om oss</a></div><img src="{A}arbete-maskiner.jpg" alt=""></section>')
add("om","B","Helbild med textkort ovanpå",f'<section class="oB" style="--img:url({A}arbete-graevning.jpg)"><div class="card"><p class="eyebrow">Om oss</p><h2>Lokalt i Skepplanda</h2><p>{om1}</p><a href="om-oss.html" class="btn">Mer om oss</a></div></section>')
add("om","C","Stort citatpåstående",f'<section class="oC"><p class="eyebrow">Om oss</p><blockquote>“Varje fastighet har sina egna förutsättningar. Därför utgår arbetet från anläggningens behov.”</blockquote><div class="cols"><p>{om1}</p><p>{om2}</p></div></section>')
add("om","D","Faktarad + text",f'<section class="oD"><div class="facts"><div><span>Bas</span><strong>Skepplanda</strong></div><div><span>Område</span><strong>Västsverige</strong></div><div><span>Återförsäljare</span><strong>BioKube</strong></div><div><span>Kontakt</span><strong>Andreas Landström</strong></div></div><div class="txt"><h2>Din partner inom avloppsteknik</h2><p>{om1} {om2}</p></div></section>')
add("om","E","Två bilder förskjutna + text",f'<section class="oE"><div class="imgs"><img src="{A}arbete-jordkallare.jpg" alt=""><img src="{A}arbete-ledningar.jpg" alt=""></div><div><p class="eyebrow">Om oss</p><h2>Från undersökning till åtgärd</h2><p>{om1}</p><p>{om2}</p><a href="om-oss.html" class="btn">Läs mer</a></div></section>')

# ---------- VARFÖR
add("varfor","A","Mörkt band, fyra kolumner",'<section class="why"><p class="eyebrow">Varför välja oss</p><h2>Rätt lösning för ditt avloppssystem</h2><div class="why-grid">'+''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t,d in WHY)+'</div></section>')
add("varfor","B","Stora nummer, lista",'<section class="sec"><h2>Varför välja oss</h2><div class="wB">'+''.join(f'<div><span>0{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(WHY))+'</div></section>')
add("varfor","C","Checklista på bild",f'<section class="wC" style="--img:url({A}arbete-maskiner.jpg)"><div class="box"><h2>Varför välja oss</h2><ul class="checks">'+''.join(f'<li><b>{t}</b> – {d}</li>' for t,d in WHY)+'</ul></div></section>')
add("varfor","D","Ljusa kort med accentkant",'<section class="sec soft"><h2>Varför välja oss</h2><div class="wD">'+''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t,d in WHY)+'</div></section>')
add("varfor","E","Accentband med stora ord",'<section class="wE">'+''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t,d in WHY)+'</section>')

# ---------- MINIRENINGSVERK
mt="Ett minireningsverk kan vara en effektiv lösning för fastigheter som saknar anslutning till kommunalt avlopp. Vi arbetar med installation av minireningsverk och relaterade VA-arbeten."
add("mini","A","Bild + text",f'<section class="oA rev"><img src="{A}arbete-jordkallare.jpg" alt=""><div><p class="eyebrow">Minireningsverk · BioKube-återförsäljare</p><h2>Moderna lösningar för enskilt avlopp</h2><p>{mt}</p><a href="minireningsverk.html" class="btn">Läs mer</a></div></section>')
add("mini","B","Mörk helbild",f'<section class="mB" style="--img:url({A}biokube.jpg)"><div><p class="eyebrow">BioKube-återförsäljare</p><h2>Enskilt avlopp utan kommunal anslutning</h2><p>{mt}</p><a href="minireningsverk.html" class="btn">Läs mer</a></div></section>')
add("mini","C","Passar för – checklista",f'<section class="sec"><div class="mC"><div><p class="eyebrow">Minireningsverk</p><h2>Passar din fastighet?</h2><p>{mt}</p><a href="minireningsverk.html" class="btn">Läs mer</a></div><ul class="checks">'+''.join(f'<li>{x}</li>' for x in SERVICES[4]["when"])+'</ul></div></section>')
add("mini","D","Stort kort med CTA",f'<section class="sec"><div class="mD"><img src="{A}biokube.jpg" alt=""><div><span class="tag">BioKube-återförsäljare</span><h2>Minireningsverk</h2><p>{mt}</p><div class="hero-cta"><a href="kontakt.html" class="btn">Kontakta oss</a><a href="tel:+4631600162" class="btn btn-outline">{TEL}</a></div></div></div></section>')
add("mini","E","Accentfärgad ruta",f'<section class="mE"><h2>Saknar fastigheten kommunalt avlopp?</h2><p>{mt}</p><a href="minireningsverk.html" class="btn">Så fungerar det →</a></section>')

# ---------- ARBETSGÅNG
add("steg","A","Fyra kolumner",'<section class="sec"><h2>Så går det till</h2>'+steps_html().replace(' class="reveal"','')+'</section>')
add("steg","B","Vertikal tidslinje",'<section class="sec"><h2>Så går det till</h2><ol class="sB">'+''.join(f'<li><span>{i+1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i,(t,d) in enumerate(STEPS))+'</ol></section>')
add("steg","C","Horisontell linje med punkter",'<section class="sec"><h2>Så går det till</h2><ol class="sC">'+''.join(f'<li><i></i><h3>{t}</h3><p>{d}</p></li>' for t,d in STEPS)+'</ol></section>')
add("steg","D","Mörk med stora siffror",'<section class="sec dark"><h2>Så går det till</h2><ol class="sD">'+''.join(f'<li><span>0{i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i,(t,d) in enumerate(STEPS))+'</ol></section>')
add("steg","E","Kort med bild överst",'<section class="sec soft"><h2>Så går det till</h2><ol class="sE">'+''.join(f'<li><img src="{A}{im}" alt=""><span>Steg {i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i,((t,d),im) in enumerate(zip(STEPS,["service.jpg","filmning.jpg","arbete-ledningar.jpg","arbete-graevning.jpg"])))+'</ol></section>')

# ---------- FAQ
add("faq","A","Enkel utfällbar lista",f'<section class="sec faq"><h2>Vanliga frågor</h2>{faq_html(FAQ)}</section>')
add("faq","B","Två kolumner",f'<section class="sec"><div class="fB"><div><h2>Vanliga frågor</h2><p>Hittar du inte svaret? Ring {TEL}.</p></div><div class="faq">{faq_html(FAQ)}</div></div></section>')
add("faq","C","Mörk",f'<section class="sec dark faq fC"><h2>Vanliga frågor</h2>{faq_html(FAQ)}</section>')
add("faq","D","Med kontaktkort bredvid",f'<section class="sec"><div class="fD"><div class="faq"><h2>Vanliga frågor</h2>{faq_html(FAQ)}</div><div class="side-card"><h3>Fler frågor?</h3><p>Andreas Landström</p><a class="big" href="tel:+4631600162">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a><a class="btn full" href="kontakt.html">Kontakta oss</a></div></div></section>')
add("faq","E","Alla svar synliga i rutnät",'<section class="sec soft"><h2>Vanliga frågor</h2><div class="fE">'+''.join(f'<div><h3>{q}</h3><p>{a}</p></div>' for q,a in FAQ)+'</div></section>')

# ---------- KONTAKT
dl=f'<dl><dt>Telefon</dt><dd><a href="tel:+4631600162">{TEL}</a></dd><dt>Mobil</dt><dd><a href="tel:+46709149718">{MOB}</a></dd><dt>E-post</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd><dt>Adress</dt><dd>{ADR}</dd><dt>Kontaktperson</dt><dd>Andreas Landström</dd></dl>'
add("kontakt","A","Uppgifter + formulär",f'<section class="contact"><div><p class="eyebrow">Kontakt</p><h2>Behöver du hjälp med ditt avlopp?</h2>{dl}</div>{form_html()}</section>')
add("kontakt","B","Stort telefonnummer",f'<section class="kB"><p class="eyebrow">Kontakt</p><h2>Ring oss</h2><a href="tel:+4631600162">{TEL}</a><p>Mobil {MOB} · {MAIL}</p></section>')
add("kontakt","C","Karta + uppgifter",f'<section class="kC"><iframe title="Karta" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=12.00%2C57.95%2C12.12%2C58.00&amp;layer=mapnik"></iframe><div><h2>Hitta oss</h2>{dl}</div></section>')
add("kontakt","D","Mörkt formulär",f'<section class="sec dark kD"><div><h2>Skicka en förfrågan</h2><p>Oavsett om du behöver undersöka ett avloppssystem, åtgärda ett problem eller installera en ny anläggning är du välkommen att kontakta oss.</p></div>{form_html()}</section>')
add("kontakt","E","Tre kontaktkort",f'<section class="sec soft"><h2>Kontakta oss</h2><div class="kE"><a href="tel:+4631600162"><span>Telefon</span><b>{TEL}</b></a><a href="tel:+46709149718"><span>Mobil</span><b>{MOB}</b></a><a href="mailto:{MAIL}"><span>E-post</span><b>{MAIL}</b></a></div></section>')

# ---------- FOOTER
add("footer","A","Mörk, tre kolumner",footer("").split('<script')[0])
add("footer","B","Stor CTA överst",f'<footer class="ftB"><h2>Behöver du hjälp med ditt avlopp?</h2><a class="phone" href="tel:+4631600162">{TEL}</a><div class="row"><span>Fastighet &amp; Avloppsteknik Väst AB · {ADR}</span><span>Org.nr 559368-4011</span></div></footer>')
add("footer","C","Minimal en rad",f'<footer class="ftC"><img src="{A}logo-transparent.png" alt="" width="32"><span>Fastighet &amp; Avloppsteknik Väst AB</span><a href="tel:+4631600162">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a><span>Org.nr 559368-4011</span></footer>')
add("footer","D","Ljus med tjänstelänkar",f'<footer class="ftD"><div><img src="{A}logo-transparent.png" alt="" width="48"><p>Avloppsteknik, VA-installationer och avloppsrening med bas i Skepplanda.</p></div><div>'+''.join(f'<a href="tjanster/{s["slug"]}.html">{s["name"]}</a>' for s in SERVICES)+f'</div><div><a href="tel:+4631600162">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a><span>{ADR}</span></div></footer>')
add("footer","E","Stor logotyptext",f'<footer class="ftE"><div class="row"><a href="tel:+4631600162">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a><span>{ADR}</span></div><div class="giant">Avloppsteknik Väst</div></footer>')

nav = ''.join(f'<a href="#{s}-A">{n}</a>' for s,n in [("hero","Hero"),("tjanster","Tjänster"),("om","Om oss"),("varfor","Varför"),("mini","Minireningsverk"),("steg","Arbetsgång"),("faq","FAQ"),("kontakt","Kontakt"),("footer","Footer")])
w("designs.html", head("Designförslag – välj per sektion","5 varianter per sektion","",'<link rel="stylesheet" href="designs.css">') +
  f'<div class="picker-top"><b>Designförslag</b> – välj en bokstav per sektion (t.ex. Hero C, Tjänster B …)<nav>{nav}</nav></div>' + ''.join(S) + '</body></html>')
print(len(S),"varianter")
