# enriquepiedfort

A single-page web tribute to **Enrique "Gato" Piedfort** — waterpolo player, coach
and dirigente.

Plain static HTML/CSS/JS with Bootstrap 5.3 from a CDN. No build step. GitHub Pages
serves the repo root from `main` and publishes to
**enriquepiedfort.waterpoloargentina.com** (see `CNAME`).

## Editing content

The **testimonios**, the **galería** and the **trayectoria** are lists in
[`data.json`](data.json) — edit them there. Some `trayectoria` milestones carry
a real photo (`img`/`alt`); milestones without one yet just omit those keys and
render as a text-only card — don't add placeholder images for them.

The rest of the copy — hero, biography, footer — lives directly
in [`index.html`](index.html). Text in `[brackets]` and spans with class `ph`
mark facts still to be filled in — years, clubs, titles, the organizing group.

Preview through a local server (`python3 -m http.server`); opening the file
directly blocks the `data.json` fetch and leaves those three sections empty.

## Local preview

```
python3 -m http.server
```

Then open <http://localhost:8000>.

## Deploy

Push to `main`. GitHub Pages redeploys automatically.
