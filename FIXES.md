# Desktop Layout Fix — Change Log

**Robert Grantham** · robertgrantham40@gmail.com · 512-200-3563
rgrantham82.github.io · Instagram [@robertgranthamart](https://instagram.com/robertgranthamart)

Repository: `rgrantham82/data-analytics-portfolio`

---

## The root cause

One line in the remote theme did all the damage:

```css
/* pages-themes/architect/_sass/jekyll-theme-architect.scss */
#main-content {
  float: left;
  width: 690px;
}
```

`_layouts/default.html` is a hand-written layout, but it still imported the
theme's stylesheet — and it named its main landmark `id="main-content"`. The
theme's ID selector (specificity 1-0-0) beat every element-level rule in
`style.scss` and turned `<main>` into a floated, fixed-width 690px column.

Two consequences, both visible in the screenshot:

1. **Content stopped filling the page.** Body text wrapped at 690px no matter
   how wide the monitor was, leaving a dead zone on the right.
2. **The footer climbed the page.** A floated element leaves normal flow, so
   the un-cleared `<footer>` rose to sit level with the top of the content and
   its centred text was shoved right by the float — landing it directly on top
   of the "About Me" heading.

---

## What changed

| # | File | Change |
|---|------|--------|
| 1 | `_layouts/default.html` | `id="main-content"` → `id="content"`; skip-link target updated to match |
| 2 | `_layouts/default.html` | Header wrapper `.inner` → `.header-inner` (the theme pins `.inner` to a fixed 940px) |
| 3 | `_layouts/default.html` | Footer content wrapped in `.footer-inner`; contact line added |
| 4 | `_layouts/default.html` | `<nav aria-label="Primary">` for screen-reader landmark clarity |
| 5 | `assets/css/style.scss` | New **Theme Neutralization** block — documented, one rule per collision |
| 6 | `assets/css/style.scss` | Flexbox sticky-footer skeleton so the footer is structurally last |
| 7 | `assets/css/style.scss` | `header h1 { width: auto }` — the theme's 540px pushed the title off-centre |
| 8 | `assets/css/style.scss` | `footer { margin-top: 0 }` — killed the theme's 40px white band |
| 9 | `assets/css/print.css` | `#main-content` → `#content` to track the rename |
| 10 | `assets/images/og-image.png` | **Created** (1200×630) — was referenced but missing |
| 11 | `assets/images/apple-touch-icon.png` | **Created** (180×180) — was referenced but missing |
| 12 | `_data/projects.yml` | Broken-link warning added above the Client Segmentation entry |

### Collisions neutralized in `style.scss`

| Theme rule | Symptom it caused |
|---|---|
| `#main-content { float: left; width: 690px }` | The layout break described above |
| `h4:before` / `h5:before` / `h6:before` (unscoped) | Pale-blue `////` on every project subtitle |
| `.inner { width: 940px }` | Header locked to a fixed width |
| `header h1 { width: 540px }` | Site title off-centre from its own tagline |
| `body { background: url(body-bg.jpg) }` | Theme texture tiled behind your white background |
| `form { padding: 20px; background: #f2f2f2 }` | Grey box around the contact form |
| `ul, ol { list-style-position: inside }` | Wrapped bullet text lost its hanging indent |
| `td { text-align: center; font-weight: 300 }` | Every table cell centred and thinned |
| `footer { margin-top: 40px }` | White gap above the footer |

---

## One judgment call you should review

Headings inside `<main>` were rendering in **Architects Daughter** with blue
slash prefixes — not by design, but because `#main-content h1` outranked your
own `h1 { font-family: 'Poppins' }`. The fix restores Poppins, which is what
`style.scss` always asked for.

If you actually liked the hand-drawn look, `style.scss` carries a commented
block showing how to opt back into it deliberately.

---

## Still open — needs your decision

1. **Client Segmentation card links to a 404.** No `client-segmentation.html`
   exists in the repo. Add the page or repoint the link.
2. **Kaggle URLs are old-format.** Links use `kaggle.com/robertgrantham/<slug>`;
   current Kaggle notebooks live at `kaggle.com/code/<user>/<slug>`. Your
   `_config.yml` also lists your Kaggle handle as `wotan587`, not
   `robertgrantham`. Worth clicking all three.
3. **Two project cards still have no image** (`police-shootings-analysis`,
   `art-sales-popup-tracker`) — the TODOs you already left in `projects.yml`.
4. **Phone number was deliberately left off the site footer.** Email, LinkedIn
   and GitHub are there. Add the number if you want it publicly crawlable.

---

## Verify after deploy

- Open the About page at 1280px+ — text should fill the column, footer should
  be at the bottom and nowhere else.
- Open the Projects page — no `////` before project subtitles.
- Paste the site URL into LinkedIn's Post Inspector — the new card should render.
- Tab from the top of any page — "Skip to content" should focus the main region.
