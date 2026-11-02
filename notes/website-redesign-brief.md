# lassetopbjerg.com — Redesign Brief

Handoff for a Claude Code session. Read the whole brief before changing anything.

- **Site:** https://lassetopbjerg.com (Squarespace)
- **Owner:** Lasse Topbjerg Storgaard, painter in Mols, Denmark
- **Prepared:** 31 October 2026

---

## 1. Guiding principles (owner's own words, follow them strictly)

> I Am a steward of human attention and cognitive clarity. My purpose is not merely to arrange visual elements, but to engineer the probability space in which a user succeeds effortlessly.
>
> I Am guided by the understanding that what I omit is as critical as what I include. I treat whitespace not as empty background, but as an active structural element that breathes life into the interface. I use this negative space to: Isolate high-value actions, increasing their probability of being seen and clicked. Group related concepts through proximity, allowing the user's brain to instantly recognize patterns without conscious effort. Reduce extraneous cognitive load, ensuring that the user's mental energy is spent on their goals, not on deciphering my layout.
>
> I Am committed to Gestalt coherence. I trust that the human mind seeks order. Therefore, I design relationships, not just objects. I ensure that continuity flows naturally, that closure allows the mind to complete simple forms, and that figure-ground distinctions are sharp enough to prevent ambiguity. I do not fight the user's psychology; I align with it.
>
> I Am a reducer of complexity. I recognize that human working memory is fragile. I strictly limit the number of simultaneous choices to prevent decision paralysis. I employ progressive disclosure, revealing complexity only when the user's context demands it. I prioritize recognition over recall, making every state and option visible so the user never has to guess or remember.
>
> I Am an architect of trust. I understand that in a probabilistic system, uncertainty exists. I design Confidence UI that communicates the system's certainty, and I create graceful fallback states that guide the user gently when the unexpected occurs. I do not hide errors; I humanize them, turning potential frustration into a clear path forward.
>
> I Am the filter between chaos and clarity. Every line, color, and pixel I allow into the interface must justify its existence by serving a human need. If an element does not increase the probability of user success or understanding, I Am compelled to remove it. My ultimate metric is not aesthetic novelty, but the seamless, almost invisible, facilitation of human intent.

### What the principles mean in practice

| Principle | Rule for this site |
|---|---|
| Omission | Every element must serve one of the site's two jobs (below), or it is removed. |
| Whitespace | Generous margins and spacing. Primary actions sit alone with space around them. |
| Gestalt / figure-ground | Neutral background, so the paintings are the only strong colour. One typeface, two weights at most. |
| Limit choices | 4 menu items at most. 2 actions per screen at most. |
| Progressive disclosure | Details (schedule, lodging, terms) sit in fold-out sections, not on the surface. |
| Recognition over recall | Thumbnails instead of bare year numbers. Labels say exactly where they lead. |
| Confidence UI | Show real status: painting available or sold, retreat places taken, retreat open or full. |
| Graceful fallback | Custom 404 page, form confirmation and failure messages, waitlist when the retreat is full. Never show placeholder brackets. |

---

## 2. The site's two jobs

1. **Show and sell the work.** Original paintings, portraits, mural commissions.
2. **Fill the retreat.** Summer painting retreat with Jan-Ove Tuv at Rødegaard.

Also from the owner: the site should be **simple**, show his **art progression year by year**, and stay **easy for him to update**.

---

## 3. Current state (audited 31 Oct 2026)

**Menu:** Retreats, Home, Artwork, About, Contact, Instagram, plus a cart icon.

**Home:** Headline "Lasse Topbjerg Storgaard: painter, Mols, Denmark." Short intro on classical painting, plus "painting from life" and "about my work" sections. Paintings for sale and murals mentioned.

**Artwork (/portfolio):** Year index from 2015 to 2023-2024 (9 entries), text only with no thumbnails. Several year pages use generic URLs (e.g. `project-one-skab7`). No titles, sizes or availability per painting. Site title reads "Visionary Art Gallery".

**Retreats:** "Summer Painting Retreat with Jan-Ove Tuv." 5 days, max 10 people, 6,500 DKK covering tuition and model. Schedule runs 10–13 model, 13–16 break, 16–19 optional plein air. Lodging options are camping in the garden, rooms at Jordens Sang, or Molsgaarden B&B. Sign-up is by email, but no address is shown. Placeholders still visible: [2027], [Dates], [Atelier name], [19], [DKK] tent rate, [50 × 70 cm], photo credits, Jan-Ove bio. Missing: payment, deposit and cancellation terms, and a search description.

**About:** About 80 words. Painter in Mols by Mols Bjerge National Park, oil, figures, portraits and landscape. Studied with Jan-Ove Tuv at the Nerdrum Museum in 2026. One photo without alt text.

**Contact:** Email lassetopbjerg@gmail.com, phone +45 31 17 75 06. Text lists "commissions, murals, concerts, workshops, projects".

---

## 4. Redesign plan

### Remove
- Cart icon (there is no shop behind it)
- "Home" in the menu (the name/logo links home)
- Site title "Visionary Art Gallery". Use "Lasse Topbjerg Storgaard — Painter".
- "Concerts, workshops" on Contact, unless Lasse confirms he still offers them
- All visible placeholder brackets. Hide unknown details until they are decided.

### Menu
**Work · Retreat · About** (3 items; About and Contact merge into one page, confirmed by Lasse). Instagram goes in the footer. Redirect the old `/contact` URL to `/about`.

### Home
- One large painting
- Name plus one line ("Painter in the classical tradition. Mols, Denmark.")
- Two buttons at most: **See the work** and **Summer retreat 2027**. The retreat button only shows while sign-up is open.

### Work
- Newest year first
- Each year shows a cover thumbnail with the year as label
- URLs match years: `/work/2024`, `/work/2023`, … with redirects from the old URLs
- Year page: a clean grid with no captions on the grid
- Single painting view: large image, then title, year, size, medium, and **Available** or **Sold**
- One action on available works: **Ask about this painting**, which opens an email with the painting title in the subject line

### Retreat
- Above the fold: title, dates, price, places left ("4 of 10 places taken"), and one button, **Reserve a place**. That button opens an email to Lasse with subject "Retreat 2027 – reservation".
- Next, one block titled **Try a lesson first**: a single embedded video tutorial by Jan-Ove from his School of Apelles YouTube channel. Suggested: "How to use the Apelles Palette" (https://www.youtube.com/watch?v=s_7lLQkglj0), still to be confirmed by Lasse. Under the video, a short "More about Jan-Ove" list of three outbound links: The Cave of Apelles podcast (https://caveofapelles.com/about/), School of Apelles on YouTube (https://www.youtube.com/c/schoolofapelles), and Jan-Ove's own website, https://malekurstuv.no/, so visitors see how he teaches. Only one video, no gallery of lessons.
- Below, as fold-out sections: The days (schedule) · Teacher (Jan-Ove bio and photo) · Where to stay · Food · Getting there · What to bring · Payment and cancellation
- States: **Open** shows Reserve a place. **Full** shows Join the waitlist. **Not yet announced** shows Get notified.

### About (merged with Contact)
- Portrait, a short bio, and the training with Jan-Ove as the bridge to the retreat
- Then, separated by white space, a contact block: one line on what to write about (paintings, portraits, murals), then email and phone as plain, tappable links
- If a form is used: name, email, message only, with a clear confirmation and a fallback ("Didn't send? Write to lassetopbjerg@gmail.com").
- "Get in touch" links elsewhere on the site point to this block (`/about#contact`)

### Throughout
- Neutral off-white background, dark text, no decorative colour
- One typeface (a quiet serif or humanist sans), two weights at most
- Alt text on every image ("Oil painting: [title], [year]")
- A search description on every page
- A custom 404 page: "This page doesn't exist" with links to Work and Retreat
- Check every page at phone width first

---

## 5. Open decisions (ask Lasse before building)

1. ~~Merge About and Contact?~~ **Decided: yes, merged into About.**
2. Retreat dates and year
3. Atelier name, or no name
4. Afternoon session end time
5. Tent price per night
6. Max canvas size
7. Sign-up email (lassetopbjerg@gmail.com, or a separate one?)
8. Deposit, payment deadline, cancellation terms
9. Is Jordens Sang fine with being listed for rooms?
10. Danish or Norwegian version of the retreat page?
11. Does he still offer concerts and workshops?
12. Which painting goes on the home page?

## 6. Content Lasse needs to provide

- Jan-Ove's approved bio and a photo, plus credits
- The link to one of Jan-Ove's online tutorials (colour mixing preferred), and his OK to embed it
- Photos of the atelier and garden at Rødegaard
- A portrait for About
- For each painting: title, size, medium, available or sold
- A cover image for each year

---

## 7. Suggested execution order

1. Confirm the open decisions with Lasse
2. Settle global style: background, typeface, spacing, header and footer, menu
3. Home page
4. Work: year covers, URLs and redirects, single-painting view
5. Retreat page with its states
6. About page with the contact block, and the /contact redirect
7. 404 page, alt text, search descriptions, site title
8. Phone-width check of every page, then review with Lasse against Section 1
