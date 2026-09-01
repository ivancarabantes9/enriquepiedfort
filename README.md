# enriquepiedfort

A single-page web tribute to **Enrique "Gato" Piedfort** — waterpolo player, coach
and dirigente — and a campaign to name the town's new pool after him.

Plain static HTML/CSS/JS with Bootstrap 5.3 from a CDN. No build step. GitHub Pages
serves the repo root from `main` and publishes to
**enriquepiedfort.waterpoloargentina.com** (see `CNAME`).

## Editing content

The **testimonios**, the **galería** and the **trayectoria** (with one image per
milestone) are lists in [`data.json`](data.json) — edit them there. Replace the
placeholder images in [`img/`](img/) (`g*` gallery, `t*` trayectoria; keep the
filenames or update `data.json`).

The rest of the copy — hero, biography, proposal, footer — lives directly in
[`index.html`](index.html). Text in `[brackets]` and spans with class `ph` mark
facts still to be filled in — years, clubs, titles, the organizing group.

Preview through a local server (`python3 -m http.server`); opening the file
directly blocks the `data.json` fetch and leaves those three sections empty.

The "Apoyar la propuesta" buttons are placeholders. A separate app will handle
verified signatures.

## Local preview

```
python3 -m http.server
```

Then open <http://localhost:8000>.

## Deploy

Push to `main`. GitHub Pages redeploys automatically.
