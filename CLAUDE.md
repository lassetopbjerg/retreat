# Retreat page — project notes for Claude Code

One-page website for Lasse Topbjerg Storgaard's summer painting retreat with Jan-Ove Tuv at Rødegaard, Mols. It is a single static file, `index.html`, hosted on GitHub Pages (same setup as Lasse's MØFFI app). Lasse's main site, lassetopbjerg.com, stays on Squarespace and its Retreat menu item should link here.

Lasse writes in Danish or English, so answer in the language he uses.

## Status (2 Nov 2026)

- **Live** at https://lassetopbjerg.github.io/retreat/ (repo `lassetopbjerg/retreat`, Pages from `main`, folder `/`). Pushing to `main` updates the site.
- Custom domain **malerefugium.dk** (bought at one.com, 3 Nov 2026) connected 3 Nov 2026: `CNAME` file in the repo, og:url/og:image point to https://malerefugium.dk/. DNS at one.com: four A records for the root to 185.199.108-111.153 and `www` CNAME to lassetopbjerg.github.io; one.com's standard A records are switched off (MX left on). The old https://lassetopbjerg.github.io/retreat/ address forwards to the domain.
- Next steps:
  4. The name in the header links to https://lassetopbjerg.com (Lasse's new site, live on that domain since 3 Nov 2026).

Deploy commands:

```bash
gh repo create lassetopbjerg/retreat --public --source . --push
gh api -X POST repos/lassetopbjerg/retreat/pages -f "source[branch]=main" -f "source[path]=/"
```

## Design (dark, since 2 Nov 2026)

- Dark, candlelit look inspired by nerdrum.com (Jan-Ove was Nerdrum's student; Lasse wants a touch of the kitsch spirit): warm umber ground #17120E, ivory text #EEE5D6, muted gold accent #C8A35E, only two typefaces (Lasse asked for fewer): Cinzel for everything that names or labels (top, headings, fold-out titles, facts, links, button), Source Serif 4 regular for running text. No italics or bold.
- Top: Smykkeskrinet as a full-height hero (whole figure visible, edges faded), with the name, "Sommer 2027 · Rødegaard" and Jan-Ove's motto over it.
- The earlier light design is tagged `foer-moerkt-design`. To go back: `git checkout foer-moerkt-design -- index.html` (text changes made since then must be redone).

## Built-in pieces (2 Nov 2026)

- Language: `#english`/`#dansk` in the link wins, then the visitor's last flag choice (localStorage), then the browser language (da/nb/nn/no/sv get Danish, everyone else English).
- Two booking buttons per language (top and after "Det praktiske"); the script fills every `.action` box.
- Footer: organiser line (name, email, phone) per language, address, Jan-Ove's Instagram; on phones also the photo credits.
- Share image `works/share.jpg` (1200x630) has the name, dates and place baked in: make a new one if any of those change. Tab icon: `favicon-32.png`, `apple-touch-icon.png`, `favicon.ico` (gold Cinzel M).
- Pictures: Jan-Ove's Ego, Smykkeskrinet, Discovery on the right; Trehøje (Mikkel Houmøller, CC BY-SA 4.0), Begtrup Vig fra Trehøje (Old Dane, CC BY-SA 4.0) and Solnedgang ved Ørby, Helgenæs (Carsten Wiehe, CC BY-SA 3.0) on the left. Side margins from 1240px wide.

## Name

The retreat is called **Malerefugium på Mols** (English: **Painting Retreat on Mols**), chosen by Lasse on 2 Nov 2026. It sits first in the line above the heading.

## How the page works

- **Two full language versions in one file, one shown at a time.** The page shows Danish by default; the flags in the header switch language (`html[data-show="da"|"en"]`), and `#english` opens the English version directly. Without JavaScript both versions show, one after the other. Every change must be made in BOTH languages.
- **Phones (< 600px) are the main audience.** Tighter spacing, facts as label/value rows, link descriptions hidden, pictures in one swipeable row, and photo credits moved from the captions to the footer. Wide screens (≥ 1340px) put the paintings in the right margin and the Mols Bjerge photos in the left.
- Settings live in the `window.RETREAT` block at the top of `index.html`:
  - `status`: `"open"` gives Reserve a place, `"full"` gives Join the waitlist, `"soon"` gives Get notified
  - `datesDa` / `datesEn` (shown in the facts and in the line over the name at the top), `placesTotal`, `placesTaken`, `email`, `paymentLink` (Stripe)
  - When `placesTaken` reaches `placesTotal`, the page switches to waitlist by itself.
- While `status` is `"open"` and `paymentLink` is set, the top button is "Reservér og betal / Reserve and pay" and goes to Stripe; the note under it has a small email link. Otherwise the button opens an email to Lasse with a prefilled subject. There is no form and no backend.
- Links to other websites open in a new tab: give every new external link `target="_blank" rel="noopener"`. The Stripe button stays in the same tab.
- Fold-out sections use native `<details>`. The video is a youtube-nocookie embed with a "watch on YouTube" fallback link.
- Only external dependencies: the Google Font Source Serif 4 (Georgia fallback) and YouTube.
- An attempt at a Pages CMS / content.json version was rejected by Lasse and reverted. Keep it a single file.

## Design principles (Lasse's own, follow them)

Lasse's principles: attention and clarity first; what is left out matters as much as what is in. Whitespace isolates the one main action. Few choices at once, and details are revealed progressively (fold-outs). Recognition over recall. Honest status: places left, open or full, with graceful fallbacks. Every element must justify its existence, so never show placeholder brackets; hide unknowns or phrase them generally instead.

Look: see "Design" above (the original light look, off-white #F4F2EE with no decorative colour, was replaced by the dark one). Works at 390px phone width with no horizontal scroll.

## Content facts (confirmed by Lasse)

- Dates: 12–16 June 2027 (Sat–Wed). Sign-up is open. Max 10 painters.
- Price: 6,000 DKK covering tuition and model. Lodging is not included.
- The model sessions are nude (akt), stated on the page since 3 Nov 2026.
- Days: 10–13 live model, 13–15 break (changed from 13–16 on 3 Nov 2026), from 15 optional plein air. The atelier is open all day and in the evening.
- Terms (confirmed): full amount paid at sign-up, no deposit; if the retreat is cancelled, all money is returned.
- Food: full board at Rødegaard 625 DKK/day, booked with Jordens Sang (kontakt@jordenssang.dk) (breakfast, lunch, dinner, tea/coffee, snacks; all vegetarian, mostly from the garden). Alternatively, a small kitchen in the atelier. No shops in Knebel; groceries in Vrinners/Ebeltoft, about 20 minutes by bus.
- Lodging: tent in the Rødegaard garden (100 DKK per night, confirmed 3 Nov 2026), rooms at Rødegaard/Jordens Sang (kontakt@jordenssang.dk), Molsgaarden B&B https://hosmolsgaarden.dk/ (Kildevej 26, Knebel).
- Getting there: Rødegaard, Karlshøjvej 5, 8420 Knebel, about 45 minutes from Aarhus. From Norway, the Larvik–Hirtshals ferry.
- Jan-Ove Tuv, from malekurstuv.no: born 1976; Odd Nerdrum's assistant 1996–2002; has run courses for 16 years (confirmed by Lasse); books on kitsch; «Jakten på Nerdrum»; podcast The Cave of Apelles; motto «Enkle regler – enkelt forklart»; reduced palette; teaches in Norwegian and English.
- Links: video https://www.youtube.com/watch?v=s_7lLQkglj0 (How to use the Apelles Palette), https://www.youtube.com/@caveofapelles, https://www.youtube.com/c/schoolofapelles, https://malekurstuv.no/
- Contact: lassetopbjerg@gmail.com, +45 31 17 75 06. Instagram on the page: Jan-Ove's @jan_ove_tuv (Lasse's own @lasse.topbjerg is not active)

## Band design (live since 3 Nov 2026)

index.html is now the full-width band design (built from the old page by tools/build_draft.py, which is no longer needed: edit index.html directly). Sections: hero, intro + facts + button, Dagene (three time slots), Trehøje photo band, Din underviser (self-portrait + bio + motto, three paintings, quiet video facade that loads YouTube on click, fold-out "Mere om Jan-Ove" with links and videos), Edith's quote band, Stedet / Rødegaard (aerial photo from jordenssang.dk; Lasse knows the owners, use is OK; Månesalen is not used for the retreat), Det praktiske fold-outs, price card at the bottom with places left. Layout rule from Lasse: headings centred, informative text left-aligned in one 720px column.

To go back to the previous single-column page: `git checkout foer-baand-design -- index.html` then commit and push (text changes made since must be redone).

## Still open

- Share image `works/share.jpg` remade 3 Nov 2026 with "Rødegaard, Vistoft" (only the top line redrawn: Cinzel Regular 21.5px, tracking 4.5, colour (185,155,100), centred at x 848.5, baseline 190).
- Price changed to 6,000 DKK on 3 Nov 2026, so it now matches the Stripe link. Stripe's public business name was "Art"; Lasse may want to fix that.
- All prices on the page are written in DKK, in both languages (Danish: "6.000 DKK", English: "6,000 DKK").
- Start time on day one and end time on day five: Lasse gives them later.
- What happens if a participant cancels: not decided yet.
- Canvas size and the afternoon end time. These are worded generally on the page.
- Jan-Ove should approve his bio and the student quote (Edith Maier Kihle).
- Ask Jordens Sang whether they are fine with being listed.
- Photos: atelier, garden, Jan-Ove, and paintings. The page has no images yet; adding one strong hero image would help.
