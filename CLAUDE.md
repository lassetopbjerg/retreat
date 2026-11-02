# Retreat page — project notes for Claude Code

One-page website for Lasse Topbjerg Storgaard's summer painting retreat with Jan-Ove Tuv at Rødegaard, Mols. It is a single static file, `index.html`, hosted on GitHub Pages (same setup as Lasse's MØFFI app). Lasse's main site, lassetopbjerg.com, stays on Squarespace and its Retreat menu item should link here.

Lasse writes in Danish or English, so answer in the language he uses.

## Status (2 Nov 2026)

- **Live** at https://lassetopbjerg.github.io/retreat/ (repo `lassetopbjerg/retreat`, Pages from `main`, folder `/`). Pushing to `main` updates the site.
- Next steps:
  4. Point the Retreat link on lassetopbjerg.com to it.
  5. Optional: custom domain retreat.lassetopbjerg.com (add a CNAME file plus a DNS CNAME record at Squarespace/the domain host).

Deploy commands:

```bash
gh repo create lassetopbjerg/retreat --public --source . --push
gh api -X POST repos/lassetopbjerg/retreat/pages -f "source[branch]=main" -f "source[path]=/"
```

## Name

The retreat is called **Malerefugium på Mols** (English: **Painting Retreat on Mols**), chosen by Lasse on 2 Nov 2026. It sits first in the line above the heading.

## How the page works

- **Two full language versions in one file, one shown at a time.** The page shows Danish by default; the flags in the header switch language (`html[data-show="da"|"en"]`), and `#english` opens the English version directly. Without JavaScript both versions show, one after the other. Every change must be made in BOTH languages.
- **Phones (< 600px) are the main audience.** Tighter spacing, facts as label/value rows, link descriptions hidden, pictures in one swipeable row, and photo credits moved from the captions to the footer. Wide screens (≥ 1340px) put the paintings in the right margin and the Mols Bjerge photos in the left.
- Settings live in the `window.RETREAT` block at the top of `index.html`:
  - `status`: `"open"` gives Reserve a place, `"full"` gives Join the waitlist, `"soon"` gives Get notified
  - `datesDa` / `datesEn`, `placesTotal`, `placesTaken`, `email`, `paymentLink` (Stripe)
  - When `placesTaken` reaches `placesTotal`, the page switches to waitlist by itself.
- While `status` is `"open"` and `paymentLink` is set, the top button is "Reservér og betal / Reserve and pay" and goes to Stripe; the note under it has a small email link. Otherwise the button opens an email to Lasse with a prefilled subject. There is no form and no backend.
- Fold-out sections use native `<details>`. The video is a youtube-nocookie embed with a "watch on YouTube" fallback link.
- Only external dependencies: the Google Font Source Serif 4 (Georgia fallback) and YouTube.
- An attempt at a Pages CMS / content.json version was rejected by Lasse and reverted. Keep it a single file.

## Design principles (Lasse's own, follow them)

Lasse's principles: attention and clarity first; what is left out matters as much as what is in. Whitespace isolates the one main action. Few choices at once, and details are revealed progressively (fold-outs). Recognition over recall. Honest status: places left, open or full, with graceful fallbacks. Every element must justify its existence, so never show placeholder brackets; hide unknowns or phrase them generally instead.

Look: off-white ground #F4F2EE, ink #1B1A18, muted #5E5A54, rules #D9D5CE, one serif typeface, no decorative colour. Works at 390px phone width with no horizontal scroll.

## Content facts (confirmed by Lasse)

- Dates: 12–16 June 2027 (Sat–Wed). Sign-up is open. Max 10 painters.
- Price: 6,500 DKK covering tuition and model. Lodging is not included.
- Days: 10–13 live model, 13–16 break, from 16 optional plein air. The atelier is open all day and in the evening.
- Terms (confirmed): full amount paid at sign-up, no deposit; if the retreat is cancelled, all money is returned.
- Food: full board at Rødegaard 625 DKK/day, booked with Jordens Sang (kontakt@jordenssang.dk) (breakfast, lunch, dinner, tea/coffee, snacks; all vegetarian, mostly from the garden). Alternatively, a small kitchen in the atelier. No shops in Knebel; groceries in Vrinners/Ebeltoft, about 20 minutes by bus.
- Lodging: tent in the Rødegaard garden (small fee), rooms at Rødegaard/Jordens Sang (kontakt@jordenssang.dk), Molsgaarden B&B https://hosmolsgaarden.dk/ (Kildevej 26, Knebel).
- Getting there: Rødegaard, Karlshøjvej 5, 8420 Knebel, about 45 minutes from Aarhus. From Norway, the Larvik–Hirtshals ferry.
- Jan-Ove Tuv, from malekurstuv.no: born 1976; Odd Nerdrum's assistant 1996–2002; has run courses for 16 years (confirmed by Lasse); books on kitsch; «Jakten på Nerdrum»; podcast The Cave of Apelles; motto «Enkle regler – enkelt forklart»; reduced palette; teaches in Norwegian and English.
- Links: video https://www.youtube.com/watch?v=s_7lLQkglj0 (How to use the Apelles Palette), https://caveofapelles.com/about/, https://www.youtube.com/c/schoolofapelles, https://malekurstuv.no/
- Contact: lassetopbjerg@gmail.com, +45 31 17 75 06, Instagram @lasse.topbjerg

## Still open

- Price is 6,500 DKK (confirmed). The Stripe link charged DKK 6,000 on 2 Nov 2026 and its public business name was "Art"; Lasse must fix both in Stripe.
- Start time on day one and end time on day five: Lasse gives them later.
- What happens if a participant cancels: not decided yet.
- Tent price per night, canvas size, and the afternoon end time. These are worded generally on the page.
- Jan-Ove should approve his bio and the student quote (Edith Maier Kihle).
- Ask Jordens Sang whether they are fine with being listed.
- Photos: atelier, garden, Jan-Ove, and paintings. The page has no images yet; adding one strong hero image would help.
