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
s = s.replace(":root {\n    --ground: #17120E;", ":root {\n    --ground: #17120E;\n    --band: #221A14;", 1)
s = s.replace("</style>", CSS + "</style>", 1)
s = s.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"', 1)

def main_block(L):
    da = L == "da"
    T = lambda d, e: d if da else e
    trehoeje = T("Nationalpark Mols Bjerge, Trehøje", "Mols Bjerge National Park, Trehøje")
    helg = T("Solnedgang ved Ørby, Helgenæs", "Sunset at Ørby, Helgenæs")
    foto = T("Foto", "Photo")
    # pull the existing blocks we keep unchanged from the live page
    m = re.search(r'<main lang="%s" data-lang="%s">(.*?)</main>' % (L, L), s, re.S).group(1)
    intro = re.search(r'<section aria-labelledby="title-%s">(.*?)</section>' % L, m, re.S).group(1)
    teacher = re.search(r'<section aria-labelledby="lesson-%s">(.*?)</section>' % L, m, re.S).group(1)
    bio = re.findall(r'<p class="lede">.*?</p>', teacher, re.S)
    video = re.search(r'<div class="video">.*?</div>', teacher, re.S).group(0)
    links = re.search(r'<div class="links".*?</div>', teacher, re.S).group(0)
    works = re.findall(r'<figure class="pos-r\d">.*?</figure>', m, re.S)
    works = [re.sub(r' class="pos-r\d"', "", w) for w in works]
    rhythm = re.search(r'<section aria-labelledby="rhythm-%s">.*?<p class="lede">(.*?)</p>' % L, m, re.S).group(1)
    faq = re.search(r'<div class="faq">(.*?)</div>\s*<div class="action action-end">', m, re.S).group(1)
    details = re.findall(r'<details.*?</details>', faq, re.S)
    keep = [d for d in details if not re.search(r'<summary>(Dagene|The days|Reservation og betaling|Reserving and paying)</summary>', d)]
    pay = [d for d in details if re.search(r'<summary>(Reservation og betaling|Reserving and paying)</summary>', d)][0]
    pay_ps = re.findall(r'<p>.*?</p>', pay, re.S)
    end_action = re.search(r'<div class="action action-end">.*?</div>', m, re.S).group(0)

    days = T(
        [("10–13", "Nøgenmodel", "Maleri efter levende nøgenmodel (akt): lys, skygge og farveblanding."),
         ("13–15", "Pause", "Frokost, hvil, en dukkert. Stranden og nationalparken ligger lige uden for døren."),
         ("15–", "Udendørs, valgfrit", "Mal i nationalparken, ved havet eller i haven på Rødegaard.")],
        [("10–13", "Nude model", "Life painting from the nude model: light, shadow and colour mixing."),
         ("13–15", "Break", "Lunch, rest, a swim. The beach and the national park are right outside the door."),
         ("15–", "Outdoors, optional", "Paint in the national park, by the sea or in the Rødegaard garden.")])
    days_html = "\n".join(
        '        <div class="day"><p class="time">%s</p><h3>%s</h3><p>%s</p></div>' % d for d in days)

    return f'''<main lang="{L}" data-lang="{L}">

  <section class="band first" aria-labelledby="title-{L}">
    <div class="inner">{intro}</div>
  </section>

  <section class="band alt" aria-labelledby="rhythm-{L}">
    <div class="inner wide">
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
    <div class="inner wide">
      <p class="eyebrow">{T("Din underviser", "Your teacher")}</p>
      <div class="teacher">
        <figure>
          <img src="works/jan-ove-selvportraet.jpg" alt="{T("Jan-Ove Tuv, selvportræt", "Jan-Ove Tuv, self-portrait")}" width="900" height="900" loading="lazy">
          <figcaption>{T("Selvportræt", "Self-portrait")}</figcaption>
        </figure>
        <div class="text">
          <h2 id="lesson-{L}">Jan-Ove Tuv</h2>
          {chr(10).join("          " + b for b in bio).strip()}
          {links}
        </div>
      </div>
      {video}
      <aside class="works" aria-label="{T("Værker af Jan-Ove Tuv", "Work by Jan-Ove Tuv")}">
        {chr(10).join("        " + w for w in works).strip()}
      </aside>
    </div>
  </section>

  <section class="band alt" aria-labelledby="price-{L}">
    <div class="inner wide">
      <p class="eyebrow">{T("Pris og tilmelding", "Price and booking")}</p>
      <div class="price-grid">
        <div>
          <p class="big" id="price-{L}">{T("6.000 DKK", "6,000 DKK")}</p>
          <p>{T("Undervisning og model i alle fem dage. Overnatning og mad er ikke inkluderet.", "Tuition and model for all five days. Accommodation and food are not included.")}</p>
        </div>
        <div>
          <h3>{T("Reservation og betaling", "Reserving and paying")}</h3>
          {chr(10).join("          " + p for p in pay_ps[:2]).strip()}
          <div class="action"><a class="button js-cta" href="mailto:lassetopbjerg@gmail.com">{T("Reservér og betal", "Reserve and pay")}</a><p class="note js-note"></p></div>
        </div>
      </div>
    </div>
  </section>


  <section class="band last" aria-labelledby="details-{L}">
    <div class="inner">
      <p class="eyebrow">{T("Det praktiske", "Practical")}</p>
      <h2 id="details-{L}">{T("Ophold, mad og rejse", "Stay, food and travel")}</h2>
      <div class="faq">
      {chr(10).join("      " + d for d in keep).strip()}
      </div>
      {end_action}
    </div>
  </section>

</main>'''

for L in ("da", "en"):
    s = re.sub(r'<main lang="%s" data-lang="%s">.*?</main>' % (L, L), lambda _: main_block(L), s, count=1, flags=re.S)

# footer photo credits: Begtrup Vig (Old Dane) is no longer used
s = re.sub(r"Mikkel Houmøller og Old Dane \((.*?)\), Carsten Wiehe \(.*?\)\.", r"Mikkel Houmøller (\1).", s)
s = re.sub(r"Mikkel Houmøller and Old Dane \((.*?)\), Carsten Wiehe \(.*?\)\.", r"Mikkel Houmøller (\1).", s)
open(out, "w", encoding="utf-8").write(s)
print("ok")
