# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-page web tribute to Enrique "Gato" Piedfort — waterpolo player, coach and dirigente, lifelong figure of **Club Gimnasia y Esgrima de Rosario** and the **Argentine Seleccionado Nacional** — plus a campaign to name **Rosario's** new municipal pool after him. Plain static HTML/CSS/JS, no build step. Bootstrap 5.3 loads from a CDN in `index.html`; `css/custom.css` is the site's own "waterline" design system layered on top.

Deliberate choices: no death date anywhere — the dates read `1945 – ∞`. The nickname is written with straight/curly double quotes ("Gato"), not guillemets.

## Structure

- `index.html` — all sections. Copy is Spanish (voseo); `[bracketed]` spans and `.ph` class mark facts still to be filled in.
- `js/app.js` — a `DATA` object at the top (`photos`, `quotes`, `timeline`) is the only thing content editors touch; the rest renders it, wires the gallery lightbox (Bootstrap modal), scroll reveals, and the nav.
- `img/*.svg` — placeholder stand-ins to be replaced with real photos (keep the filenames or update `DATA.photos`).
- `img/og.jpg` — the social-card image (1200×630), composed from `img/gato_profile.png`. Referenced by the `og:image` / `twitter:image` tags with explicit width/height. Regenerate it if that source photo or the name/dates change.
- `assets/qr/` — QR code (vector + raster) pointing at the live URL, for a printed banner. `qr-marca.svg` is also shown in the on-page "Compartir" section. `LEER.md` there explains which file to send to print. Regenerate with `segno` if the URL changes.
- The "Apoyar la propuesta" / "Descargar carta" buttons are **placeholders** — a separate verified-voting app will own real signatures. Do not wire a real form into this repo.

## Deploy

GitHub Pages serves the repo root from `main`. Any push to `main` publishes the live site at `enriquepiedfort.waterpoloargentina.com`. There is no staging environment; test locally by opening `index.html` in a browser.

## Formatting

`npm run format` (Prettier) formats HTML/CSS/JS/MD. Run it before committing. Requires `npm install` first (Node is not preinstalled on this machine — `sudo snap install node --classic`).

## Gotchas

- `CNAME` pins the custom domain. Do not delete or edit it — removing it breaks the domain mapping on the next deploy.
- Preview with `python3 -m http.server` (Node/npm are not installed on this machine; `file://` also works but a server matches production).
