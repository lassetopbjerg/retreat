# Retreat page — project notes for Claude Code

One-page website for **Malerefugium på Mols** (English: **Painting Retreat on Mols**), Lasse Topbjerg Storgaard's summer painting retreat with Jan-Ove Tuv at Rødegaard, Vistoft (Mols). A single static file, `index.html`, hosted on GitHub Pages. Lasse's own site, https://lassetopbjerg.com (repo `lassetopbjerg/Lassetopbjerg`, also GitHub Pages), links here from its menu and footer.

Lasse writes in Danish or English, so answer in the language he uses.

## Status (4 Nov 2026)

- **Live on https://malerefugium.dk** since 3 Nov 2026. Repo `lassetopbjerg/retreat`, Pages from `main`, folder `/`; the `CNAME` file holds the domain; og:url / og:image point to https://malerefugium.dk/. The old https://lassetopbjerg.github.io/retreat/ address forwards to the domain. Pushing to `main` updates the site.
- **DNS at one.com** (domain bought there 3 Nov 2026): four A records for the root to 185.199.108.153 / .109.153 / .110.153 / .111.153 and `www` CNAME to `lassetopbjerg.github.io`; one.com's standard A records are switched off, MX left on.
- The name in the header links to https://lassetopbjerg.com.
- If a Pages deploy fails with a GitHub 503 ("No server is currently available"), it is GitHub's fault: re-run it, or push an empty commit if the re-run hangs in the queue.

## Design (dark, since 2 Nov 2026)

- Dark, candlelit look inspired by nerdrum.com (Jan-Ove was Nerdrum's assistant; Lasse wants a touch of the kitsch spirit): warm umber ground #17120E, ivory text #EEE5D6, muted gold accent #C8A35E. Two typefaces only: Cinzel for everything that names or labels, Source Serif 4 regular for running text. No italics or bold.
- **Band design** (live since 3 Nov 2026): full-width bands, top to bottom:
  1. Hero: Smykkeskrinet (whole figure visible, edges faded), with "9.–13. juni 2027 · Rødegaard, Vistoft", the name and Jan-Ove's motto.
     (No flame up here: it was tried in the hero and in the header on 10 Nov 2026 and moved to the footer, see Footer below.)
  2. Intro, facts and the first booking button.
  3. Dagene: three time slots.
  4. Trehøje photo band.
  5. Din underviser: self-portrait, bio in two paragraphs (the second in Lasse's own words, added 4 Nov 2026; the 16 years, motto and reduced palette moved into the "Mere om Jan-Ove" fold-out on 10 Nov 2026 to cut text), seven works in a sliding row (Ego, Smykkeskrinet, Discovery, Selvportræt med stråhat, Studie til «Ghaiur», Kranie, Gammel kvinde; the last four restored 4 Nov 2026 from commit c4eda9e^ at Lasse's wish for more works), shown whole at a fixed height (360px, 280px on phones) with ‹ › buttons from 600px (`.works-nav`), then a quiet video facade that loads YouTube on click, and one fold-out "Mere om Jan-Ove" with links and videos.
  6. Edith's quote band.
  7. Stedet / Rødegaard: aerial photo from jordenssang.dk (Lasse knows the owners, use is OK; Månesalen is not used for the retreat). Below it, one fold-out "Oplev Mols og Helgenæs / Explore Mols and Helgenæs" (added 4 Nov 2026): things to see and do, grouped as Nationalpark Mols Bjerge, Helgenæs, Ebeltoft og Kalø (`.area-label` headings), facts from nationalparkmolsbjerge.dk and Wikipedia. Every place name links to a Google Maps search (photos and directions); a "Læs mere / Read more" line links the national park site and Wikipedia for Helgenæs and Ebeltoft. Official sites of single places (Glasmuseet, Fregatten Jylland, Sletterhage Fyr) could not be verified from the cloud session; add them if Lasse confirms the addresses.
  8. Det praktiske: fold-outs.
  9. Price card at the bottom, with places left and the second booking button.
- **Sticky section menu** under the header (`.secnav`, one per language): Dagene · Underviser · Stedet · Praktisk · Tilmelding / The days · Teacher · The place · Practical · Booking, linking to #dagene #underviser #stedet #praktisk #tilmelding (#the-days #teacher #the-place #practical #booking). Only #english / #dansk change the language.
- **Layout rule from Lasse:** headings centred, informative text left-aligned in one 720px column. Wider blocks (teacher, works row, aerial photo, price card) share one width, 880px; captions align with what they belong to. All fold-out lists use the gold dashes of the price card.
- **Type system** (block at the end of the CSS), keep to these sizes:
  - labels: Cinzel 13px, 0.2em, uppercase, gold
  - headings (h1, h2): Cinzel, uppercase, 0.08em
  - fold-out titles and link titles: Cinzel 18px, 0.04em, mixed case
  - reading text: Source Serif 4 18px; small text 15px; captions 13px
- **Earlier designs are saved as git tags:** `foer-baand-design` (single-column dark page) and `foer-moerkt-design` (light page). To go back: `git checkout <tag> -- index.html`, then commit and push. Text changes made since then must be redone.
- Some side-margin CSS for `.works` (min-width 1240px) is left over from the old layout; harmless. The unused pictures and `tools/build_draft.py` were removed 10 Nov 2026.

## How the page works

- **Two full language versions in one file, one shown at a time.** Danish by default; the flags in the header switch language (`html[data-show="da"|"en"]`). Language choice: `#english`/`#dansk` in the link, then the visitor's last flag choice (localStorage), then the browser language (da/nb/nn/no/sv get Danish, everyone else English). Without JavaScript both versions show, one after the other. **Every change must be made in BOTH languages.**
- **Phones (< 600px) are the main audience.** Works at 390px with no horizontal scroll.
- **Settings** live in the `window.RETREAT` block at the top of `index.html`:
  - `status`: `"open"` gives Reserve a place, `"full"` gives Join the waitlist, `"soon"` gives Get notified.
  - `datesDa` / `datesEn`, `placesTotal`, `placesTaken`, `email`, `priceDkk` (used for the NOK conversion; the price in the text must be changed by hand too).
  - When `placesTaken` reaches `placesTotal`, the page switches to waitlist by itself.
  - While `placesTaken` is 0 the page says "Kun 10 pladser / Only 10 places" (Lasse's wording, 10 Nov 2026, to make it feel exclusive) and hides the dots; from the first sign-up it shows "9 af 10 ledige" and the dots (10 Nov 2026).
- **Booking:** two `.action` boxes per language (after the intro, and in the price card); the script fills both. The button opens an email to Lasse with a prefilled subject and body (name, phone, number of places, how they heard about the retreat: used for the marketing plan's tracking); the note under it is short ("Åbner en mail til Lasse. Eller skriv til <address>.", 10 Nov 2026), with the address as a link for visitors without a mail app. The Tilmelding / Booking link in the sticky menu is gold (`.secnav-cta`). Lasse replies with Jan-Ove's bank details, the materials list and practical information, and updates `placesTaken` by hand. Participants pay by bank transfer directly to Jan-Ove (decided 9 Nov 2026; Stripe removed). Never put the bank details on the page. There is no form and no backend.
- **Links:** every external link gets `target="_blank" rel="noopener"`. "Getting there" has a button that opens Rødegaard in Maps.
- **Prices** are always written in DKK, in both languages: Danish "7.020 DKK", English "7,020 DKK".
- **Currency button** (added 9 Nov 2026): under the price in both the price card and the hero fact (both stay in sync), switches the retreat price between DKK and approximate NOK. Fetches the rate on each switch from api.frankfurter.dev (ECB, updated once per working day), with open.er-api.com as backup; no API key. If both fail, the price stays in DKK and a short message shows. Lodging and food prices stay in DKK.
- Fold-out sections use native `<details>`.
- **External dependencies:** Google Fonts (Cinzel, Source Serif 4; Georgia fallback), YouTube (youtube-nocookie, loaded on click) and the video's still image from i.ytimg.com behind the play button (`.video-thumb`; tries maxresdefault, then mqdefault, and removes itself if it fails; not verified from the cloud session).
- **Photos for phones:** the Trehøje band and the Rødegaard aerial photo have 1200px versions (`-1200.jpg`) picked through `srcset`; if either photo is replaced, remake both sizes.
- **Works row:** a "1 / 7" counter (`.works-count`) under the row, on phones without the arrows.
- **Flame** (`.flame` in `.flame-wrap`, 10 Nov 2026, Lasse's wish): a small pixel-art flame centred at the bottom of the scene (`.scene`) that closes the page, just above the footer text. One inline SVG on an 11 × 15 pixel grid with six frames (`<g>`), shown one at a time by CSS (`flame-frame`, 0.15s per frame), a soft glow behind, and eight small square "pixel" sparks (`.flame i`) that drift gently out to both sides. Under prefers-reduced-motion it shows the first frame only and the sparks are hidden. Under the flame sits two crossed pixel logs with embers (`.logs`, 17 × 6 pixels, an X in front of the base of the flame, added the same day so it reads as a bonfire); the flame rises out of it. The flame is a `<button>`: a tap starts or stops a fire sound (low rumble, hiss and random crackles), made in the browser with Web Audio in the last `<script>`, so there is no sound file; it stops when the tab is hidden. With the fire comes a quiet, wordless mumble of two low voices taking turns (`murmur()`, added the same evening at Lasse's wish): each voice is a buzzing tone with a little breath noise through two vowel filters, muffled, with a sing-song phrase melody (low then up inside each word, sinking through the phrase, to suggest Norwegian) and an occasional "mm" from the listener. Lasse found the first version too robotic, so it now has a constant random pitch wobble, gliding pitch, syllables that run together in words, and varied lengths and loudness. The voices are generic and synthetic, not modelled on or sampled from Jan-Ove's or Nerdrum's real voices. The sound could not be listened to from the cloud session, only checked for errors.
- **Two pixel figures by the fire** (`.sitter`, `.sit-l` / `.sit-r` in `.flame-wrap`, 10 Nov 2026, Lasse's wish): small seated figures on each side of the flame, meant as Jan-Ove Tuv (left: brown felt hat, grey beard, brown scarf, grey jacket, dark red trousers, after a third photo from Lasse) and Odd Nerdrum (right: pale straw hat with a wide brim, white hair at the sides, off-white smock). Drawn by hand on a 10 × 13 pixel grid, with clothes and colours taken from photos Lasse sent on 10 Nov 2026; they are decorative, unnamed and hidden from screen readers. Each has a `.lit` group of warm pixels on the side facing the fire (face and body) whose opacity flickers in steps (`firelight`), like light from the flames. Nerdrum is not part of the retreat, so Lasse was told to check with Jan-Ove (and ideally Nerdrum) that the figure is fine.
- **Night sky** (`.sky`, first child of the footer, 10 Nov 2026, Lasse's wish): a deep blue night sky filling the scene above the fire (`.scene` has 150px of top padding for it). It starts 140px above the footer and fades in through a mask, and the footer's top rule was removed for it. 64 small square stars (`.sky i`, positions and timings as inline styles, generated once) shimmer with the `twinkle` animation; they stand still under prefers-reduced-motion. At the bottom of the sky is a slightly curved horizon (`.sky::after`, added the same day at Lasse's wish): the top of a very wide ellipse of dark ground with a faint warm light along its edge; the fire and the two figures sit on it. Along the horizon stand pixel silhouettes of pine trees (`.pine`, inline SVGs in `.sky`, 3px pixels; ten on phones and 14 more from 760px, `.pine.wide`), placed left and right of the fire with their bottoms following the curve (positions and heights as inline styles, generated once); the sky is a little lighter just above the horizon so they stand out. The pines sway gently (`sway`, a small skew from the base, at three different speeds). Five dim pixel clouds (`.cloud`, inline SVGs first in `.sky`, so they pass behind the trees) drift slowly from left to right across the sky at different heights and speeds (`drift`, 120–230s per crossing), added 10 Nov 2026 in place of two walking figures of Plato and Aristotle that Lasse tried and removed. Scene content sits above the sky (`.scene > * { z-index: 1 }`).
- **The whole fire scene is an Easter egg** (Lasse, 10 Nov 2026): keep it at the very bottom and never announce it in the page text. The only pointer is a subtle hint (`.hint`, near the top of the scene, where the sky fades in under the price card): a small gold pixel arrow that bobs slowly at low opacity; a tap jumps to the fire (`#baal` on `.flame-wrap`).
- **Footer:** two parts since 10 Nov 2026 (Lasse: "put organiser and that info all the way down the bottom"). First `.scene`: the night sky, the hint arrow and the fire with the two figures on the curved horizon. Then `.foot-text`, the very last thing on the page, on the dark ground colour below the horizon: organiser line (name, email, phone) per language, address, Jan-Ove's Instagram, and on phones also the photo credits. Rules that used to say `footer > …` now say `.scene > …`.
- **Share image** `works/share.jpg` (2400x1260 since 11 Nov 2026, double size so it is sharp on phones; rebuilt by measuring the old 1200x630 one: Smykkeskrinet scaled to full height at x=40 (1x), colours multiplied by (0.692, 0.724, 0.778), faded at both sides; text redrawn in Cinzel. A sharper photo of Smykkeskrinet from Jan-Ove would improve it most) has the name, dates and "Rødegaard, Vistoft" baked in; make a new one if any of those change, and bump the `?v=` on the og:image URL so Facebook refetches it. Top line redrawn 3 Nov and 6 Nov 2026 (new dates); Cinzel can be fetched from npm (`@fontsource/cinzel`, convert the woff2 to TTF with fonttools). The line is drawn (Cinzel Regular 21.5px, tracking 4.5, colour (185,155,100), centred at x 848.5, baseline 190).
- **Tab icon:** `favicon-32.png`, `apple-touch-icon.png`, `favicon.ico` (gold Cinzel M).
- **Photo credits:** Trehøje by Mikkel Houmøller (CC BY-SA 4.0); the Rødegaard aerial photo comes from jordenssang.dk. The two room photos in the lodging fold-out (`works/roedegaard-vaerelse-1.jpg`, `-2.jpg`, 600x600, added 8 Nov 2026) come from https://roedegaard-mols.dk/overnatning/; use approved by Lasse.
- A Pages CMS / content.json version was rejected by Lasse and reverted. Keep it a single file.

- **Shops in "What to bring"** (9 Nov 2026): Jotun (Ebeltoft, Google Maps link) and Aart de Vos (Aarhus, aartdevos.dk) each get their own line (`.shops` / `.shop` / `.shop-name`, Cinzel 18px gold, like link titles) with place and what they sell, so they are easy to spot.

## Design principles (Lasse's own, follow them)

Attention and clarity first; what is left out matters as much as what is in. Whitespace isolates the one main action. Few choices at once, and details are revealed progressively (fold-outs). Recognition over recall. Honest status: places left, open or full, with graceful fallbacks. Every element must justify its existence, so never show placeholder brackets; hide unknowns or phrase them generally instead.

## Content facts (confirmed by Lasse)

- **Dates:** 9–13 June 2027 (Wed–Sun; changed from 12–16 June on 6 Nov 2026). Sign-up is open. Max 10 painters.
- **Price:** 7,020 DKK covering tuition and model (changed from 6,000 on 9 Nov 2026). Lodging is not included.
- **Model:** the model sessions are nude (akt), stated plainly on the page.
- **What to bring** (fold-out, added 4 Nov 2026, short beginner version of Jan-Ove's PDF "Materialliste 2024" from his email of 14 Oct 2026): oil paint in black, white, yellow and red; medium (linseed oil + turpentine or odourless thinner); palette and cup; a handful of flat brushes, stiff and soft; one or two canvases up to 50 × 70 cm; an easel that can go outdoors (participants can borrow one from Lasse if they ask in advance, 9 Nov 2026); rags, charcoal, a small hand mirror. Names two shops (added 9 Nov 2026): Jotun in Ebeltoft (https://maps.app.goo.gl/79JL4d9Cj398v71AA), a 20-minute drive from Rødegaard, with a limited range of oil paint, mediums, canvas, canvas boards and brushes; and Aart de Vos in Aarhus (https://aartdevos.dk/) for anything more specific. Ends with: a more detailed list with brands is sent after sign-up (Lasse forwards it with the bank details).
- **Included** (price card list): 5 days of teaching with Jan-Ove; live nude model every morning 10–13; plenty of time for feedback from Jan-Ove; open studio all day and evening; teaching videos from Jan-Ove before the course to prepare; plenty of time to enjoy the area; a creative community where we learn from one another (last two added by Lasse 8 Nov 2026). Do not list the materials list there.
- **Days:** three cards (Lasse tried four cards in a 2 × 2 grid on 11 Nov 2026 and preferred three). 10–13 morning meeting and live model (10–10.45 "morgenmøde / morning meeting": talk about painting and thinking about it, practical questions, especially day one, and feedback on what people painted in their free time; Jan-Ove, 11 Nov 2026), 13–15 break, from 15 painting on your own (Jan-Ove does not teach then, but people may watch him paint, indoors or out; card "Åbent Atelier / Open Studio", wording by Lasse and Jan-Ove, 11 Nov 2026: paint yourself or watch Jan-Ove; landscape subjects if the weather allows, otherwise indoors in the studio; "no teaching during these hours" comes last). The atelier is open all day and in the evening. Participants may bring their own creative projects to work on in the afternoons and evenings (line under the time slots, added 4 Nov 2026). The same paragraph says there is room for spontaneous outings and cosy evenings around the campfire (added 9 Nov 2026; merged into one paragraph in normal reading text 10 Nov 2026).
- **Terms:** full amount paid at sign-up, no deposit; if the retreat is cancelled, all money is returned. If a participant has to withdraw from 9 May 2027 onwards, compensation is a place on Tuv's six-week online portrait course (Jan-Ove's wording, 11 Nov 2026). Before 9 May they get their money back (Lasse), but the page deliberately does not say so (Lasse removed that line).
- **Food:** full board at Rødegaard 625 DKK/day, booked with Jordens Sang (kontakt@jordenssang.dk): breakfast, lunch, dinner, tea/coffee and snacks, all vegetarian, mostly from the garden. Single meals (only lunch, dinner or whatever is needed) can also be arranged. Alternatively, a small kitchen in the atelier. No shops in Knebel; groceries in Vrinners/Ebeltoft, about 20 minutes by bus.
- **Lodging:**
  - tent in the Rødegaard garden, 125 DKK per day (changed from 100 per night, 5 Nov 2026)
  - rooms at Rødegaard: single 650 DKK, double 1,000 DKK per day (confirmed by Lasse 5 Nov 2026); the page says rooms with own shower and toilet are available, not that all have them (Lasse, 10 Nov 2026); booked with Jordens Sang (kontakt@jordenssang.dk; Lasse confirmed 10 Nov 2026 that this is the right address, not the one on roedegaard-mols.dk)
  - Molsgaarden B&B, https://hosmolsgaarden.dk/ (Kildevej 26, Knebel), a bed and breakfast 2 minutes' walk from Rødegaard (Lasse, 8 Nov 2026)
- **Getting there** (fold-out "Sådan kommer du hertil / Getting there"): Rødegaard, Karlshøjvej 5, 8420 Knebel, about 45 minutes from Aarhus. A "Fra Norge / From Norway" part (added 4 Nov 2026, Lasse wants it there, not in a separate fold-out):
  - ferry Kristiansand–Hirtshals (Fjord Line, Color Line) from about 2½ h
  - ferry Larvik–Hirtshals (Color Line) from about 3¾ h
  - Hirtshals to Rødegaard about 2½ h by car
  - with a car it is easy to bring easel and canvases, and people can share the car; or fly to Aarhus, Billund or Copenhagen and go on by train or bus
- **Text trim, 10 Nov 2026** (Lasse felt the page was getting text-heavy): the intro is one paragraph, the days section has one sentence above the slots and one merged paragraph below, and the bio is two paragraphs. Keep visible text short; put extra facts in fold-outs.
- **Opening line** of the intro (Lasse, 10 Nov 2026): "For første gang i Danmark afholder Jan-Ove Tuv, tidligere assistent og elev hos Odd Nerdrum, et malekursus." / "For the first time in Denmark, Jan-Ove Tuv, former assistant and student of Odd Nerdrum, is holding a painting course." It continues: "Mal efter nøgenmodel og udforsk landskabet i og omkring Mols Bjerge." (Lasse's wording). Nerdrum links to nerdrum.com.
- **Norwegian participants** are a main audience (Lasse, 4 Nov 2026): make it easy for them to say yes. The intro says the teaching is in Norwegian and English, and the place section says Ebeltoft is about 20 minutes away by car or bus (10 Nov 2026).
- **Jan-Ove Tuv** (from malekurstuv.no):
  - born 1976
  - Odd Nerdrum's assistant 1996–2002
  - has run courses for 16 years
  - books on kitsch
  - «Jakten på Nerdrum», linked to nerdrum.com: Danish → /nb/produkt/jakten-paa-nerdrum-2018/, English → /movies/the-hunt-of-odd-nerdrum-2018/
  - podcast The Cave of Apelles
  - motto «Enkle regler – enkelt forklart»
  - reduced palette
  - teaches in Norwegian and English
- **Links:**
  - video https://www.youtube.com/watch?v=s_7lLQkglj0 (How to use the Apelles Palette)
  - https://www.youtube.com/@caveofapelles
  - https://www.youtube.com/c/schoolofapelles
  - https://malekurstuv.no/
- **Contact:** lassetopbjerg@gmail.com, +45 31 17 75 06, shown in the footer and in the last fold-out of Det praktiske, "Spørgsmål? / Questions?" (added 8 Nov 2026). Instagram on the page is Jan-Ove's @jan_ove_tuv; Lasse's own @lasse.topbjerg is not active.
- **Visit counter:** GoatCounter (cookie-free, no cookie banner needed), script tag at the end of `<head>`. Stats at https://malerefugium.goatcounter.com (Lasse's account, added 11 Nov 2026). The `?kilde=` links show up as separate paths there.
- **Facebook page** "Malerefugium på Mols" (https://www.facebook.com/profile.php?id=61596512578874), created 11 Nov 2026: category Kunstskole, gold-text profile picture, the share image as cover. No posts yet; nothing goes out before the January launch. Jan-Ove OK'd using his images in marketing (11 Nov 2026).
- **Marketing:** the marketing plan is a Claude Doc, "Marketing plan: Malerefugium på Mols" (https://claude.ai/artifact/LPd1JVyaEzFHsiZZg7aCK8).

## Still open

- **Sign-up email (not on the page), from Jan-Ove 11 Nov 2026:** every participant should get 1) the materials list ("Materialliste 2026.pdf", attached to his email of 11 Nov 2026), 2) payment info (his corrected IBAN/BIC from that email; the account he gave on 8 Nov was wrong), 3) the video links he sent before his Nerdrum Museum course. Jan-Ove needs the participants' email addresses. Mention that oily rags should be burned each evening (if Rødegaard has a fire pit).
- Jan-Ove asks whether a Danish shop (Jotun Ebeltoft or Aart de Vos) would give his students a discount, as sembkunstogrammer.no gives Norwegians 10%; if so, add it to the page and he adds it to the PDF.
- Compare "What to bring" with Materialliste 2026.pdf (the page is based on the 2024 list).
- **Payment details still to settle:**
  - who refunds if the retreat is cancelled
  - currency
  - how Lasse's costs (model, marketing) are covered
  - when a place counts as secured: at the email or at payment
  - deactivate the old Stripe payment link in Stripe
- Start time on day one: Lasse gives it later. (Sunday, the last day, ends at 13:00, and people travelling from far away should arrive the day before: a second after-days line under Dagene, Lasse 11 Nov 2026.)
- The afternoon end time; worded generally on the page.
- Sign-up deadline: not set.
- Ask Jan-Ove whether the small pixel figure of Odd Nerdrum by the fire is fine with him and with Nerdrum.
- Jan-Ove should approve his bio and the student quote (Edith Maier Kihle). (His paintings in marketing: OK, 11 Nov 2026.)
- Ask Jordens Sang whether they are fine with being listed, and to confirm full board for up to 10 people.
- Lasse's own photos of the atelier, the garden and a painting set-up would strengthen the page.
