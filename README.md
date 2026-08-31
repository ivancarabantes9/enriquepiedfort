# enriquepiedfort

A single-page web tribute to **Enrique "Gato" Piedfort** — waterpolo player, coach
and dirigente — and a campaign to name the town's new pool after him.

Plain static HTML/CSS/JS with Bootstrap 5.3 from a CDN. No build step. GitHub Pages
serves the repo root from `main` and publishes to
**enriquepiedfort.waterpoloargentina.com** (see `CNAME`).

## Editing content

Everything an editor needs is in one place: the `DATA` object at the top of
[`js/app.js`](js/app.js) — the photo gallery, the testimonial quotes, and the
career timeline. Replace the placeholder images in [`img/`](img/) (keep the
filenames, or update `DATA.photos`).

Prose copy (the hero, the biography, the proposal) lives in
[`index.html`](index.html). Text in `[brackets]` and spans with class `ph` mark
facts still to be filled in — years, clubs, titles, the city, the organizing group.

The "Apoyar la propuesta" buttons are placeholders. A separate app will handle
verified signatures.

## Local preview

```
python3 -m http.server
```

Then open <http://localhost:8000>.

## Deploy

Push to `main`. GitHub Pages redeploys automatically.
