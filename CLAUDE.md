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
  2. Intro, facts and the first booking button.
  3. Dagene: three time slots.
  4. Trehøje photo band.
  5. Din underviser: self-portrait, bio (incl. a paragraph in Lasse's own words on Jan-Ove's wide knowledge and making complex ideas easy to digest, added 4 Nov 2026) and motto, seven works in a sliding row (Ego, Smykkeskrinet, Discovery, Selvportræt med stråhat, Studie til «Ghaiur», Kranie, Gammel kvinde; the last four restored 4 Nov 2026 from commit c4eda9e^ at Lasse's wish for more works), shown whole at a fixed height (360px, 280px on phones) with ‹ › buttons from 600px (`.works-nav`), then a quiet video facade that loads YouTube on click, and one fold-out "Mere om Jan-Ove" with links and videos.
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
- `tools/build_draft.py` built the band design from the old page and is no longer needed: edit index.html directly. Some files in works/ are no longer used (helgenaes-solnedgang.jpg, mols-bjerge-begtrup-vig.jpg, mols-bjerge-trehoeje.jpg), and some side-margin CSS for `.works` (min-width 1240px) is left over from the old layout.

## How the page works

- **Two full language versions in one file, one shown at a time.** Danish by default; the flags in the header switch language (`html[data-show="da"|"en"]`). Language choice: `#english`/`#dansk` in the link, then the visitor's last flag choice (localStorage), then the browser language (da/nb/nn/no/sv get Danish, everyone else English). Without JavaScript both versions show, one after the other. **Every change must be made in BOTH languages.**
- **Phones (< 600px) are the main audience.** Works at 390px with no horizontal scroll.
- **Settings** live in the `window.RETREAT` block at the top of `index.html`:
  - `status`: `"open"` gives Reserve a place, `"full"` gives Join the waitlist, `"soon"` gives Get notified.
  - `datesDa` / `datesEn`, `placesTotal`, `placesTaken`, `email`, `priceDkk` (used for the NOK conversion; the price in the text must be changed by hand too).
  - When `placesTaken` reaches `placesTotal`, the page switches to waitlist by itself.
- **Booking:** two `.action` boxes per language (after the intro, and in the price card); the script fills both. The button opens an email to Lasse with a prefilled subject; Lasse replies with Jan-Ove's bank details, the materials list and practical information, and updates `placesTaken` by hand. Participants pay by bank transfer directly to Jan-Ove (decided 9 Nov 2026; Stripe removed). Never put the bank details on the page. There is no form and no backend.
- **Links:** every external link gets `target="_blank" rel="noopener"`. "Getting there" has a button that opens Rødegaard in Maps.
- **Prices** are always written in DKK, in both languages: Danish "7.020 DKK", English "7,020 DKK".
- **Currency button** (added 9 Nov 2026): under the price in both the price card and the hero fact (both stay in sync), switches the retreat price between DKK and approximate NOK. Fetches the rate on each switch from api.frankfurter.dev (ECB, updated once per working day), with open.er-api.com as backup; no API key. If both fail, the price stays in DKK and a short message shows. Lodging and food prices stay in DKK.
- Fold-out sections use native `<details>`.
- **External dependencies:** Google Fonts (Cinzel, Source Serif 4; Georgia fallback) and YouTube (youtube-nocookie, loaded on click).
- **Footer:** organiser line (name, email, phone) per language, address, and Jan-Ove's Instagram; on phones also the photo credits.
- **Share image** `works/share.jpg` (1200x630) has the name, dates and "Rødegaard, Vistoft" baked in; make a new one if any of those change, and bump the `?v=` on the og:image URL so Facebook refetches it. Top line redrawn 3 Nov and 6 Nov 2026 (new dates); Cinzel can be fetched from npm (`@fontsource/cinzel`, convert the woff2 to TTF with fonttools). The line is drawn (Cinzel Regular 21.5px, tracking 4.5, colour (185,155,100), centred at x 848.5, baseline 190).
- **Tab icon:** `favicon-32.png`, `apple-touch-icon.png`, `favicon.ico` (gold Cinzel M).
- **Photo credits:** Trehøje by Mikkel Houmøller (CC BY-SA 4.0); the Rødegaard aerial photo comes from jordenssang.dk. The two room photos in the lodging fold-out (`works/roedegaard-vaerelse-1.jpg`, `-2.jpg`, 600x600, added 8 Nov 2026) come from https://roedegaard-mols.dk/overnatning/; use approved by Lasse.
- A Pages CMS / content.json version was rejected by Lasse and reverted. Keep it a single file.

## Design principles (Lasse's own, follow them)

Attention and clarity first; what is left out matters as much as what is in. Whitespace isolates the one main action. Few choices at once, and details are revealed progressively (fold-outs). Recognition over recall. Honest status: places left, open or full, with graceful fallbacks. Every element must justify its existence, so never show placeholder brackets; hide unknowns or phrase them generally instead.

## Content facts (confirmed by Lasse)

- **Dates:** 9–13 June 2027 (Wed–Sun; changed from 12–16 June on 6 Nov 2026). Sign-up is open. Max 10 painters.
- **Price:** 7,020 DKK covering tuition and model (changed from 6,000 on 9 Nov 2026). Lodging is not included.
- **Model:** the model sessions are nude (akt), stated plainly on the page.
- **What to bring** (fold-out, added 4 Nov 2026, short beginner version of Jan-Ove's PDF "Materialliste 2024" from his email of 14 Oct 2026): oil paint in white, yellow ochre, red and black; medium (linseed oil + turpentine or odourless thinner); palette and cup; a handful of flat brushes, stiff and soft; one or two canvases up to 50 × 70 cm; an easel that can go outdoors; rags, charcoal, a small hand mirror. Names two shops (added 9 Nov 2026): Jotun in Ebeltoft (https://maps.app.goo.gl/79JL4d9Cj398v71AA), a 20-minute drive from Rødegaard, with a limited range of oil paint, mediums, canvas, canvas boards and brushes; and Aart de Vos in Aarhus (https://aartdevos.dk/) for anything more specific. Ends with: a more detailed list with brands is sent after sign-up (Lasse forwards it with the bank details).
- **Included** (price card list): 5 days of teaching with Jan-Ove; live nude model every morning 10–13; plenty of time for feedback from Jan-Ove; open studio all day and evening; teaching videos from Jan-Ove before the course to prepare; plenty of time to enjoy the area; a creative community where we learn from one another (last two added by Lasse 8 Nov 2026). Do not list the materials list there.
- **Days:** 10–13 live model, 13–15 break, from 15 optional plein air. The atelier is open all day and in the evening. Participants may bring their own creative projects to work on in the afternoons and evenings (line under the time slots, added 4 Nov 2026).
- **Terms:** full amount paid at sign-up, no deposit; if the retreat is cancelled, all money is returned.
- **Food:** full board at Rødegaard 625 DKK/day, booked with Jordens Sang (kontakt@jordenssang.dk): breakfast, lunch, dinner, tea/coffee and snacks, all vegetarian, mostly from the garden. Alternatively, a small kitchen in the atelier. No shops in Knebel; groceries in Vrinners/Ebeltoft, about 20 minutes by bus.
- **Lodging:**
  - tent in the Rødegaard garden, 125 DKK per day (changed from 100 per night, 5 Nov 2026)
  - rooms at Rødegaard, private bathroom and toilet: single 650 DKK, double 1,000 DKK per day (confirmed by Lasse 5 Nov 2026); booked with Jordens Sang (kontakt@jordenssang.dk)
  - Molsgaarden B&B, https://hosmolsgaarden.dk/ (Kildevej 26, Knebel), a bed and breakfast 2 minutes' walk from Rødegaard (Lasse, 8 Nov 2026)
- **Getting there** (fold-out "Sådan kommer du hertil / Getting there"): Rødegaard, Karlshøjvej 5, 8420 Knebel, about 45 minutes from Aarhus. A "Fra Norge / From Norway" part (added 4 Nov 2026, Lasse wants it there, not in a separate fold-out):
  - ferry Kristiansand–Hirtshals (Fjord Line, Color Line) from about 2½ h
  - ferry Larvik–Hirtshals (Color Line) from about 3¾ h
  - Hirtshals to Rødegaard about 2½ h by car
  - with a car it is easy to bring easel and canvases, and people can share the car; or fly to Aarhus, Billund or Copenhagen and go on by train or bus
- **Norwegian participants** are a main audience (Lasse, 4 Nov 2026): make it easy for them to say yes. The intro says the teaching is in Norwegian and English, and the place section says Ebeltoft is about 20 minutes away.
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
- **Marketing:** the marketing plan is a Claude Doc, "Marketing plan: Malerefugium på Mols" (https://claude.ai/artifact/LPd1JVyaEzFHsiZZg7aCK8).

## Still open

- **Payment details still to settle:**
  - who refunds if the retreat is cancelled
  - currency
  - how Lasse's costs (model, marketing) are covered
  - when a place counts as secured: at the email or at payment
  - deactivate the old Stripe payment link in Stripe
- Start time on day one and end time on day five: Lasse gives them later.
- What happens if a participant cancels: not decided yet.
- The afternoon end time; worded generally on the page.
- Sign-up deadline: not set.
- Jan-Ove should approve his bio and the student quote (Edith Maier Kihle), and his paintings' use in marketing.
- Ask Jordens Sang whether they are fine with being listed, and to confirm full board for up to 10 people.
- Lasse's own photos of the atelier, the garden and a painting set-up would strengthen the page.
- Check with Rødegaard: the page says rooms have a private bathroom, but roedegaard-mols.dk says only some do and others share. That site also gives kontakt@roedegaard-mols.dk, while the page uses kontakt@jordenssang.dk.
