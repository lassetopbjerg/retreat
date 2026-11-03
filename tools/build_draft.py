import re, sys
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()

CSS = r"""
  /* ===== Draft: full-width bands that break the page into clear parts ===== */
  main { max-width: none; padding: 0; display: block; gap: 0; }
  .band { padding: 96px 16px; }
  .band.alt { background: var(--band); }
  .band.first { padding-top: clamp(24px, 6vw, 56px); }
  .band.last { padding-bottom: 120px; }
  .inner { width: 100%; max-width: 760px; margin: 0 auto; display: flex; flex-direction: column; gap: 24px; }
  .inner.wide { max-width: 1040px; }
  .eyebrow { margin: 0 0 -12px; font-family: var(--caps); font-size: 13px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--gold); }
  .band h2 { font-size: clamp(22px, 3vw, 30px); letter-spacing: 0.08em; color: var(--ink); }
  .days { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; margin-top: 16px; }
  .day { border-top: 1px solid var(--rule); padding-top: 20px; }
  .day .time { margin: 0 0 10px; font-family: var(--caps); font-size: 34px; line-height: 1; color: var(--gold); font-variant-numeric: lining-nums; }
  .day h3 { margin: 0 0 8px; font-family: var(--caps); font-weight: 400; font-size: 16px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink); }
  .day p { margin: 0; color: var(--body); font-size: 17px; }
  .after-days { margin: 8px 0 0; color: var(--muted); font-size: 16px; }
  .photo-band { margin: 0; position: relative; }
  .photo-band img { display: block; width: 100%; height: clamp(260px, 48vw, 620px); object-fit: cover; filter: brightness(0.82) saturate(0.85); }
  .photo-band img[src*="trehoeje"] { object-position: 50% 32%; }
  .photo-band figcaption { max-width: 1040px; margin: 0 auto; padding: 10px 16px 0; font-size: 13px; color: var(--muted); }
  .photo-band figcaption a { color: var(--muted); }
  .teacher { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 48px; align-items: start; }
  .teacher figure { margin: 0; }
  .teacher figure img { display: block; width: 100%; height: auto; box-shadow: 0 0 0 1px rgba(238, 229, 214, 0.08); }
  .teacher figcaption { margin-top: 8px; font-size: 13px; color: var(--muted); }
  .teacher .text { display: flex; flex-direction: column; gap: 20px; }
  .teacher .lede { margin: 0; }
  .band .works { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; align-items: start; position: static; }
  .band .works figure { position: static; width: auto; }
  .band .works img { aspect-ratio: 4 / 5; object-fit: cover; }
  .price-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: start; }
  .price-grid > div { display: flex; flex-direction: column; gap: 16px; }
  .big { margin: 0; font-family: var(--caps); font-size: clamp(40px, 6vw, 58px); line-height: 1; color: var(--ink); }
  .price-grid p { margin: 0; color: var(--body); }
  .price-grid > div:first-child { padding-top: 0; }
  .price-grid h3 { min-height: 0; margin: 0; font-family: var(--caps); font-weight: 400; font-size: 13px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--gold); }
  @media (max-width: 799px) {
    .days, .teacher, .price-grid { grid-template-columns: 1fr; gap: 28px; }
    .teacher figure { max-width: 360px; }
  }
  @media (max-width: 599px) {
    .band { padding: 64px 16px; }
    .band.first { padding-top: 24px; }
    .day .time { font-size: 28px; }
    .band .works { display: flex; gap: 12px; overflow-x: auto; scroll-snap-type: x mandatory; margin: 0 -16px; padding: 0 16px 4px; scrollbar-width: none; }
    .band .works figure { flex: none; width: 62%; scroll-snap-align: start; }
    .photo-band img { height: 56vw; min-height: 220px; }
  }
"""
EXTRA = r"""
  /* ===== Draft round 2: one left edge, quote band, the place, quieter video ===== */
  .inner, .inner.wide { max-width: 1040px; }
  .inner > h1, .inner > h2, .inner > .lede, .inner > .facts, .inner > .action, .inner > .faq, .inner > .after-days, .inner > .video-intro, .inner > .video-facade, .inner > .video { max-width: 720px; }
  .video-facade { display: block; position: relative; width: 100%; aspect-ratio: 16 / 9; text-decoration: none;
    background: radial-gradient(ellipse at 50% 45%, #2A2019 0%, #120E0B 70%); box-shadow: 0 0 0 1px rgba(238, 229, 214, 0.08); }
  .video-facade .play { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 14px; color: var(--ink); text-align: center; padding: 16px; }
  .video-facade .play-icon { width: 76px; height: 76px; border-radius: 50%; border: 1px solid var(--gold); display: grid; place-items: center; }
  .video-facade .play-icon::after { content: ""; margin-left: 6px; border-left: 20px solid var(--gold); border-top: 12px solid transparent; border-bottom: 12px solid transparent; }
  .video-facade:hover .play-icon { background: rgba(200, 163, 94, 0.12); }
  .video-facade .play-title { font-family: var(--caps); font-size: clamp(18px, 2.4vw, 24px); letter-spacing: 0.1em; text-transform: uppercase; }
  .video-facade .play-sub { font-size: 15px; color: var(--muted); }
  .quote-band blockquote { margin: 0 auto; max-width: 860px; text-align: center; }
  .quote-band blockquote p { margin: 0; font-size: clamp(24px, 3.4vw, 36px); line-height: 1.4; color: var(--ink); text-wrap: balance; }
  .quote-band cite { display: block; margin-top: 24px; font-style: normal; font-family: var(--caps); font-size: 13px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--gold); }
  .place-hero { margin: 8px 0 0; }
  .place-hero img { display: block; width: 100%; height: clamp(240px, 42vw, 560px); object-fit: cover; }
  .band .works.place-grid img { aspect-ratio: 4 / 3; }
  .photo-credit { margin: 0; font-size: 13px; color: var(--muted); }
  .places-line { margin: 0; font-family: var(--caps); font-size: 18px; letter-spacing: 0.06em; color: var(--ink); }
  .price-grid .dots { margin-top: -8px; }
  .teach-more { border-top: 1px solid var(--rule); max-width: 720px; }
  @media (max-width: 799px) { .teacher figure { max-width: 240px; } }
  @media (max-width: 599px) { .quote-band blockquote p { font-size: 22px; } .video-facade .play-icon { width: 60px; height: 60px; } }

  /* ===== Draft round 3: everything on one centre line ===== */
  .inner > * { width: 100%; margin-left: auto; margin-right: auto; }
  .inner > .eyebrow, .inner > h1, .inner > h2, .inner > .lede, .inner > .after-days, .inner > .video-intro, .inner > .photo-credit { max-width: 720px; text-align: center; }
  .inner > .eyebrow { margin-bottom: -12px; }
  .inner > .facts, .inner > .action, .inner > .faq, .inner > .video-facade, .inner > .video { max-width: 720px; }
  .inner > .action { align-items: center; text-align: center; }
  .fact { align-items: center; text-align: center; }
  .facts .dots { justify-content: center; }
  .day { text-align: center; }
  .price-grid { grid-template-columns: 1fr; max-width: 720px; margin: 0 auto; gap: 24px; text-align: center; }
  .price-grid > div { align-items: center; }
  .price-grid .dots { justify-content: center; margin-top: -8px; }
  .price-grid .action { align-items: center; }
  .teach-more { max-width: 720px; }
  .teacher { max-width: 1040px; margin-top: 8px; }
  .teacher .text { padding-top: 4px; }
  @media (max-width: 599px) {
    .fact { align-items: baseline; text-align: left; }
    .facts .dots { justify-content: flex-start; }
  }
"""
s = s.replace(":root {\n    --ground: #17120E;", ":root {\n    --ground: #17120E;\n    --band: #221A14;", 1)
s = s.replace("</style>", CSS + EXTRA + "</style>", 1)
s = s.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1)

def main_block(L):
    da = L == "da"
    T = lambda d, e: d if da else e
    trehoeje = T("Nationalpark Mols Bjerge, Trehøje", "Mols Bjerge National Park, Trehøje")
    foto = T("Foto", "Photo")
    m = re.search(r'<main lang="%s" data-lang="%s">(.*?)</main>' % (L, L), s, re.S).group(1)
    intro = re.search(r'<section aria-labelledby="title-%s">(.*?)</section>' % L, m, re.S).group(1)
    teacher = re.search(r'<section aria-labelledby="lesson-%s">(.*?)</section>' % L, m, re.S).group(1)
    bio = re.findall(r'<p class="lede">.*?</p>', teacher, re.S)
    bio[0] = bio[0].replace("Jan-Ove Tuv (f. 1976) er", "Jan-Ove (f. 1976) er").replace("Jan-Ove Tuv (b. 1976) is", "Jan-Ove (b. 1976) is")
    video_intro = bio.pop(2).replace('class="lede"', 'class="lede video-intro"')
    vtitle = re.search(r'<iframe[^>]*title="([^"]*)"', teacher).group(1)
    links = re.search(r'<div class="links".*?</div>', teacher, re.S).group(0)
    works = re.findall(r'<figure class="pos-r\d">.*?</figure>', m, re.S)
    works = [re.sub(r' class="pos-r\d"', "", w) for w in works]
    faq = re.search(r'<div class="faq">(.*?)</div>\s*<div class="action action-end">', m, re.S).group(1)
    details = re.findall(r'<details.*?</details>', faq, re.S)
    def has(d, *names): return re.search(r'<summary>(%s)</summary>' % "|".join(names), d)
    teach = [d for d in details if has(d, "Sådan underviser han", "How he teaches")][0]
    quote_m = re.search(r'\s*<p>[«“](.*?)[»”] — (.*?)</p>', teach, re.S)
    teach = teach.replace(quote_m.group(0), "")
    keep = [d for d in details if not has(d, "Dagene", "The days", "Reservation og betaling", "Reserving and paying", "Sådan underviser han", "How he teaches")]
    pay = [d for d in details if has(d, "Reservation og betaling", "Reserving and paying")][0]
    pay_ps = re.findall(r'<p>.*?</p>', pay, re.S)

    days = T(
        [("10–13", "Nøgenmodel", "Maleri efter levende nøgenmodel (akt): lys, skygge og farveblanding."),
         ("13–15", "Pause", "Frokost, hvil, en dukkert. Stranden og nationalparken ligger lige uden for døren."),
         ("15–", "Udendørs, valgfrit", "Mal i nationalparken, ved havet eller i haven på Rødegaard.")],
        [("10–13", "Nude model", "Life painting from the nude model: light, shadow and colour mixing."),
         ("13–15", "Break", "Lunch, rest, a swim. The beach and the national park are right outside the door."),
         ("15–", "Outdoors, optional", "Paint in the national park, by the sea or in the Rødegaard garden.")])
    days_html = "\n".join('        <div class="day"><p class="time">%s</p><h3>%s</h3><p>%s</p></div>' % d for d in days)
    rhythm = T("Formiddagen er undervisning, resten af dagen er din egen. Mols er kendt for sine unikke og smukke landskaber, og det er svært ikke at blive inspireret af naturen her.",
               "Mornings are taught, the rest of the day is yours. Mols is known for its unique and beautiful landscapes, and it is hard not to feel inspired here.")
    place_grid = [
        ("works/roedegaard-maanesalen.jpg", 1400, 1179, T("Månesalen på Rødegaard, et lyst rum under det hvide loft", "The Moon Hall at Rødegaard, a bright room under the white rafters"), T("Månesalen", "The Moon Hall")),
        ("works/roedegaard-indenfor.jpg", 1400, 1050, T("Lyst fællesrum med borde og store vinduer ud mod haven", "Bright common room with tables and large windows onto the garden"), T("Fællesrummet", "The common room")),
        ("works/roedegaard-haven.jpg", 1400, 934, T("Morgenfruer foran det lyserøde hus på Rødegaard", "Marigolds in front of the pink house at Rødegaard"), T("Haven", "The garden")),
    ]
    grid_html = "\n".join('        <figure><img src="%s" alt="%s" width="%d" height="%d" loading="lazy"><figcaption>%s</figcaption></figure>' % (f, a, w, h, c) for f, w, h, a, c in place_grid)

    return f'''<main lang="{L}" data-lang="{L}">

  <section class="band first" aria-labelledby="title-{L}">
    <div class="inner">{intro}</div>
  </section>

  <section class="band alt" aria-labelledby="rhythm-{L}">
    <div class="inner">
      <p class="eyebrow">{T("Dagene", "The days")}</p>
      <h2 id="rhythm-{L}"><span class="nowrap">{T("Tid til læring –", "Time to learn –")}</span> <span class="nowrap">{T("tid til fordybelse", "time to immerse yourself")}</span></h2>
      <p class="lede">{rhythm}</p>
      <div class="days">
{days_html}
      </div>
      <p class="after-days">{T("Atelieret er åbent hele dagen og om aftenen.", "The studio is open all day and into the evening.")}</p>
    </div>
  </section>

  <figure class="photo-band">
    <img src="works/mols-bjerge-trehoeje-wide.jpg" alt="{T("Lyngklædte bakker og Trehøje i Nationalpark Mols Bjerge", "Heather-covered hills and Trehøje in Mols Bjerge National Park")}" width="2400" height="1591" loading="lazy">
    <figcaption>{trehoeje}. <a href="https://commons.wikimedia.org/wiki/File:Treh%C3%B8je_Mols_Bjerge.jpg" target="_blank" rel="noopener">{foto}: Mikkel Houmøller</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener">CC BY-SA 4.0</a></figcaption>
  </figure>

  <section class="band" aria-labelledby="lesson-{L}">
    <div class="inner">
      <p class="eyebrow">{T("Din underviser", "Your teacher")}</p>
      <h2 id="lesson-{L}">Jan-Ove Tuv</h2>
      <div class="teacher">
        <figure>
          <img src="works/jan-ove-selvportraet.jpg" alt="{T("Jan-Ove Tuv, selvportræt", "Jan-Ove Tuv, self-portrait")}" width="900" height="900" loading="lazy">
          <figcaption>{T("Selvportræt", "Self-portrait")}</figcaption>
        </figure>
        <div class="text">
          {chr(10).join("          " + b for b in bio).strip()}
          {links}
        </div>
      </div>
      {video_intro}
      <a class="video-facade" href="https://www.youtube.com/watch?v=s_7lLQkglj0" target="_blank" rel="noopener" data-embed="https://www.youtube-nocookie.com/embed/s_7lLQkglj0?autoplay=1" data-title="{vtitle}">
        <span class="play"><span class="play-icon" aria-hidden="true"></span><span class="play-title">{T("Apelles-paletten", "The Apelles palette")}</span><span class="play-sub">{T("Video med Jan-Ove Tuv · YouTube", "Video with Jan-Ove Tuv · YouTube")}</span></span>
      </a>
      <aside class="works" aria-label="{T("Værker af Jan-Ove Tuv", "Work by Jan-Ove Tuv")}">
        {chr(10).join("        " + w for w in works).strip()}
      </aside>
      <div class="faq teach-more">
        {teach}
      </div>
    </div>
  </section>

  <section class="band alt quote-band" aria-label="{T("Fra en tidligere elev", "From a former student")}">
    <div class="inner">
      <blockquote><p>{T("«", "“")}{quote_m.group(1)}{T("»", "”")}</p><cite>{quote_m.group(2)}</cite></blockquote>
    </div>
  </section>

  <section class="band" aria-labelledby="place-{L}">
    <div class="inner">
      <p class="eyebrow">{T("Stedet", "The place")}</p>
      <h2 id="place-{L}">Rødegaard</h2>
      <p class="lede">{T("Rødegaard ligger i Vistoft ved Nationalpark Mols Bjerge, med bakker, skov og hav tæt på. Her holder Jordens Sang til, og det er også dem, der laver maden.", "Rødegaard is in Vistoft, by Mols Bjerge National Park, with hills, woods and the sea close by. It is home to Jordens Sang, who also cook the food.")}</p>
      <figure class="place-hero"><img src="works/roedegaard-luftfoto.jpg" alt="{T("Rødegaard set fra luften, med haven, gårdens bygninger og bakkerne bagved", "Rødegaard from the air, with the garden, the farm buildings and the hills behind")}" width="2400" height="1598" loading="lazy"></figure>
      <p class="photo-credit">{T("Fotos", "Photos")}: <a href="https://jordenssang.dk/" target="_blank" rel="noopener">Jordens Sang</a></p>
    </div>
  </section>

  <section class="band alt" aria-labelledby="details-{L}">
    <div class="inner">
      <p class="eyebrow">{T("Det praktiske", "Practical")}</p>
      <h2 id="details-{L}">{T("Ophold, mad og rejse", "Stay, food and travel")}</h2>
      <div class="faq">
      {chr(10).join("      " + d for d in keep).strip()}
      </div>
    </div>
  </section>

  <section class="band last" aria-labelledby="price-{L}">
    <div class="inner">
      <p class="eyebrow">{T("Pris og tilmelding", "Price and booking")}</p>
      <div class="price-grid">
        <div>
          <p class="big" id="price-{L}">{T("6.000 DKK", "6,000 DKK")}</p>
          <p>{T("Undervisning og model i alle fem dage. Overnatning og mad er ikke inkluderet.", "Tuition and model for all five days. Accommodation and food are not included.")}</p>
        </div>
        <div>
          <p class="places-line js-places2"></p>
          <div class="dots js-dots2" aria-hidden="true"></div>
          {pay_ps[1]}
          <p>{T("Efter tilmelding får du materialeliste og praktisk information fra Lasse.", "After you sign up, Lasse will send you the materials list and practical information.")}</p>
          <div class="action"><a class="button js-cta" href="mailto:lassetopbjerg@gmail.com">{T("Reservér og betal", "Reserve and pay")}</a><p class="note js-note"></p></div>
        </div>
      </div>
    </div>
  </section>

</main>'''

for L in ("da", "en"):
    s = re.sub(r'<main lang="%s" data-lang="%s">.*?</main>' % (L, L), lambda _: main_block(L), s, count=1, flags=re.S)

# footer photo credits: only Trehøje from Wikimedia, plus Jordens Sang
s = re.sub(r"Mikkel Houmøller og Old Dane \((.*?)\), Carsten Wiehe \(.*?\)\.", r"Mikkel Houmøller (\1). Fotos af Rødegaard: Jordens Sang.", s)
s = re.sub(r"Mikkel Houmøller and Old Dane \((.*?)\), Carsten Wiehe \(.*?\)\.", r"Mikkel Houmøller (\1). Photos of Rødegaard: Jordens Sang.", s)

SCRIPT = """<script>
  (function () {
    // Price band: repeat places left + dots from the facts row
    document.querySelectorAll("main[data-lang]").forEach(function (main) {
      var a = main.querySelector(".js-places"), b = main.querySelector(".js-places2");
      if (a && b) b.textContent = a.textContent;
      var d1 = main.querySelector(".js-dots"), d2 = main.querySelector(".js-dots2");
      if (d1 && d2) d2.innerHTML = d1.innerHTML;
    });
    // Video: load YouTube only when clicked
    document.querySelectorAll(".video-facade").forEach(function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var box = document.createElement("div"); box.className = "video";
        var f = document.createElement("iframe");
        f.src = a.getAttribute("data-embed"); f.title = a.getAttribute("data-title");
        f.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"; f.allowFullscreen = true;
        box.appendChild(f); a.replaceWith(box);
      });
    });
  })();
</script>
</body>"""
s = s.replace("</body>", SCRIPT, 1)
open(out, "w", encoding="utf-8").write(s)
print("ok")
