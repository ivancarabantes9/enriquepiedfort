/* ===========================================================================
   Enrique "Gato" Piedfort — homenaje
   Editá SOLO el objeto DATA de abajo para cambiar fotos, testimonios y años.
   El resto arma la página, la galería con lightbox y las animaciones.
   =========================================================================== */

const DATA = {
  /* Galería. Poné las imágenes en img/ y listalas acá, de la más a la menos
     importante. year y caption son opcionales. */
  photos: [
    { src: "img/g1.svg", year: "[año]", caption: "[Qué pasa en esta foto. Reemplazar por una imagen real.]" },
    { src: "img/g2.svg", year: "[año]", caption: "[Descripción de la foto.]" },
    { src: "img/g3.svg", year: "[año]", caption: "[Descripción de la foto.]" },
    { src: "img/g4.svg", year: "[año]", caption: "[Descripción de la foto.]" },
    { src: "img/g5.svg", year: "[año]", caption: "[Descripción de la foto.]" },
    { src: "img/g6.svg", year: "[año]", caption: "[Descripción de la foto.]" }
  ],

  /* Testimonios. quote = la frase; who = quién lo dice; role = su relación con él. */
  quotes: [
    { quote: "[Testimonio de un jugador o jugadora que formó.]", who: "[Nombre]", role: "Jugó bajo su dirección en Gimnasia y Esgrima" },
    { quote: "[Testimonio de un colega entrenador.]", who: "[Nombre]", role: "Entrenador" },
    { quote: "[Testimonio de un dirigente del club o del Seleccionado.]", who: "[Nombre]", role: "Dirigente" },
    { quote: "[Unas palabras de la familia.]", who: "[Nombre]", role: "Familia" }
  ],

  /* Trayectoria. En orden cronológico. */
  timeline: [
    { year: "[196X]", label: "Primeros pasos en el agua, en el Club Gimnasia y Esgrima de Rosario." },
    { year: "[197X]", label: "Debuta con el Seleccionado Nacional." },
    { year: "[198X]", label: "Se retira como jugador y empieza a dirigir en Gimnasia y Esgrima." },
    { year: "[200X]", label: "Asume como [cargo] del club." },
    { year: "[201X]", label: "[Reconocimiento o hito destacado.]" },
    { year: "∞", label: "Su legado sigue en cada categoría formativa del club y en el waterpolo de Rosario." }
  ]
};

/* --------------------------------------------------------------------------- */

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

function renderQuotes() {
  const grid = document.getElementById("quoteGrid");
  if (!grid) return;
  DATA.quotes.forEach((q) => {
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

function renderGallery() {
  const wrap = document.getElementById("gallery");
  if (!wrap) return;
  DATA.photos.forEach((p, i) => {
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

function renderTimeline() {
  const ol = document.getElementById("timeline");
  if (!ol) return;
  DATA.timeline.forEach((t) => {
    ol.append(
      h("li", {},
        h("span", { class: "t-year", text: t.year }),
        h("span", { class: "t-label", text: t.label })
      )
    );
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
    } catch {
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
      } catch {
        ok = false;
      }
    }
    if (ok) flashCopied();
    else window.prompt("Copiá el enlace:", url);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  renderQuotes();
  renderGallery();
  renderTimeline();
  initLightbox();
  initReveal();
  initNav();
  initShare();
  initPlaceholders();
});
