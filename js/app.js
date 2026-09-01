/* ===========================================================================
   Enrique "Gato" Piedfort — homenaje

   Los TESTIMONIOS, la GALERÍA y la TRAYECTORIA se editan en  ../data.json
   El resto del texto del sitio está directo en index.html.

   Nota: abierto con doble clic (file://) el navegador no deja leer data.json
   y esas tres secciones quedan vacías. Para la vista real:
   `python3 -m http.server` y entrá por http://localhost:8000
   =========================================================================== */

async function loadData() {
  try {
    const res = await fetch("data.json", { cache: "no-cache" });
    if (!res.ok) throw new Error("HTTP " + res.status);
    return await res.json();
  } catch (err) {
    console.warn(
      "No se pudo leer data.json (testimonios, galería y trayectoria quedan vacíos).",
      location.protocol === "file:"
        ? "Abrí el sitio con un servidor local: python3 -m http.server"
        : err
    );
    return {};
  }
}

const h = (tag, attrs = {}, ...kids) => {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") el.className = v;
    else if (k === "text") el.textContent = v;
    else if (v != null) el.setAttribute(k, v);
  }
  for (const kid of kids) if (kid) el.append(kid);
  return el;
};

function renderQuotes(items) {
  const grid = document.getElementById("quoteGrid");
  if (!grid || !Array.isArray(items)) return;
  grid.textContent = "";
  items.forEach((q) => {
    const cite = h("cite", { text: q.who });
    if (q.role) cite.append(h("span", { text: q.role }));
    grid.append(
      h("div", { class: "col-md-6 col-lg-3" },
        h("figure", { class: "quote-card" },
          h("p", { text: "“" + q.quote + "”" }),
          cite
        )
      )
    );
  });
}

function renderGallery(items) {
  const wrap = document.getElementById("gallery");
  if (!wrap || !Array.isArray(items)) return;
  wrap.textContent = "";
  items.forEach((p, i) => {
    const btn = h("button", {
      class: "shot",
      type: "button",
      "data-year": p.year || "",
      "data-caption": p.caption || "",
      "aria-label": "Ampliar foto" + (p.caption ? ": " + p.caption : " " + (i + 1))
    }, h("img", { src: p.src, alt: p.caption || "Foto de Enrique Piedfort", loading: "lazy" }));
    wrap.append(btn);
  });
}

function renderTimeline(items) {
  const ol = document.getElementById("timeline");
  if (!ol || !Array.isArray(items)) return;
  ol.textContent = "";
  items.forEach((t) => {
    const card = h("div", { class: "t-card reveal" }, h("span", { class: "t-year", text: t.year }));
    if (t.img) {
      card.append(
        h("div", { class: "t-media" },
          h("img", { src: t.img, alt: t.alt || "", loading: "lazy" }))
      );
    }
    card.append(h("p", { class: "t-label", text: t.label }));
    ol.append(h("li", { class: t.img ? "t-item" : "t-item t-item-coda" }, card));
  });
}

function initLightbox() {
  const modalEl = document.getElementById("lightbox");
  const gallery = document.getElementById("gallery");
  if (!modalEl || !gallery || !window.bootstrap) return;

  const modal = new bootstrap.Modal(modalEl);
  const img = document.getElementById("lightboxImg");
  const cap = document.getElementById("lightboxCaption");

  gallery.addEventListener("click", (e) => {
    const shot = e.target.closest(".shot");
    if (!shot) return;
    const full = shot.querySelector("img");
    img.src = full.src;
    img.alt = full.alt;
    const year = shot.dataset.year ? shot.dataset.year + " · " : "";
    cap.textContent = year + (shot.dataset.caption || "");
    modal.show();
  });
}

function initReveal() {
  const items = document.querySelectorAll(".reveal");
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) {
    items.forEach((el) => el.classList.add("in"));
    return;
  }
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in");
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
  items.forEach((el) => io.observe(el));
}

function initNav() {
  const nav = document.getElementById("nav");
  if (!nav) return;
  const onScroll = () => nav.classList.toggle("scrolled", window.scrollY > 40);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // cerrar el menú colapsado al elegir una sección (mobile)
  nav.querySelectorAll(".nav-link, .navbar-brand, .btn").forEach((link) => {
    link.addEventListener("click", () => {
      const open = nav.querySelector(".navbar-collapse.show");
      if (open && window.bootstrap) bootstrap.Collapse.getOrCreateInstance(open).hide();
    });
  });
}

function initPlaceholders() {
  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  // CTA de apoyo: todavía no hay backend de voto verificado.
  const msg = "El sistema de apoyo verificado abre muy pronto. " +
    "Mientras tanto, escribinos a [correo@ejemplo.com] para sumarte.";
  ["supportCta", "letterCta"].forEach((id) => {
    const el = document.getElementById(id);
    if (!el) return;
    el.addEventListener("click", (e) => {
      e.preventDefault();
      window.alert(msg);
    });
  });
}

function initShare() {
  const url = "https://enriquepiedfort.waterpoloargentina.com";
  const text = "Homenaje a Enrique “Gato” Piedfort y la propuesta para que el nuevo natatorio de Rosario lleve su nombre.";

  const wa = document.getElementById("shWhatsapp");
  if (wa) wa.href = "https://wa.me/?text=" + encodeURIComponent(text + " " + url);

  const copyBtn = document.getElementById("copyLink");
  if (!copyBtn) return;

  const flashCopied = () => {
    copyBtn.classList.add("copied");
    clearTimeout(copyBtn._t);
    copyBtn._t = setTimeout(() => copyBtn.classList.remove("copied"), 2200);
  };

  copyBtn.addEventListener("click", async () => {
    let ok = false;
    try {
      await navigator.clipboard.writeText(url);
      ok = true;
    } catch (e1) {
      try {
        const ta = document.createElement("textarea");
        ta.value = url;
        ta.setAttribute("readonly", "");
        ta.style.position = "absolute";
        ta.style.left = "-9999px";
        document.body.appendChild(ta);
        ta.select();
        ok = document.execCommand("copy");
        document.body.removeChild(ta);
      } catch (e2) {
        ok = false;
      }
    }
    if (ok) flashCopied();
    else window.prompt("Copiá el enlace:", url);
  });
}

document.addEventListener("DOMContentLoaded", async () => {
  const data = await loadData();
  renderQuotes(data.testimonios);
  renderGallery(data.galeria);
  renderTimeline(data.trayectoria);
  initLightbox();
  initReveal();
  initNav();
  initShare();
  initPlaceholders();
});
