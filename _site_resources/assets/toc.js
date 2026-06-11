document.addEventListener("DOMContentLoaded", function () {
  var toc     = document.getElementById("toc-list");
  var empty   = document.getElementById("toc-empty");
  var content = document.querySelector(".doc-content");
  if (!toc || !empty || !content) { return; }

  // If Python pre-populated the TOC (render_site.py build_toc_html),
  // the list already has children — hide the empty notice and stop.
  if (toc.children.length > 0) {
    empty.hidden = true;
    return;
  }

  // Dynamic fallback: build TOC from headings found in the article body.
  // Currently h2-only, matching the Python build_toc_html() logic.
  // To enable h3 entries, uncomment the h3 selector line and the
  // li.className assignment line below, then make the matching change
  // in build_toc_html() in render_site.py so both paths stay in sync.
  var headings = content.querySelectorAll("h2[id]");
  // var headings = content.querySelectorAll("h2[id], h3[id]");

  headings.forEach(function (h) {
    var li = document.createElement("li");
    li.className = "toc-h2";
    // if (h.tagName.toLowerCase() === "h3") li.className = "toc-h3";
    var a = document.createElement("a");
    a.href        = "#" + h.id;
    a.textContent = h.textContent;
    li.appendChild(a);
    toc.appendChild(li);
  });

  empty.hidden = toc.children.length > 0;
});


// ── Sidebar toggle for narrow viewports ──────────────────────────────────────
//
// Controls the collapsible sidebar emitted by render_page() in render_site.py.
// On wide viewports (> 960px) the toggle button is display:none via CSS and
// this code is effectively idle.
//
// Required elements (present only on pages from render_site.py):
//   <button id="sidebar-toggle-btn">   toggle button
//   <div    id="sidebar-inner">        collapsible content
//
// Exits immediately if either element is absent so the QRG page
// (generate_bdq_qrg_filtering.py), which manages its own sidebar via a
// native <details>/<summary>, is completely unaffected.
//
// Without JS: the <noscript> block in page.html forces
//   #sidebar-inner  { display: block !important }
//   .sidebar-toggle { display: none  !important }
// so the TOC remains reachable and the non-functional button is hidden.
(function () {
  "use strict";

  var btn   = document.getElementById("sidebar-toggle-btn");
  var inner = document.getElementById("sidebar-inner");
  if (!btn || !inner) { return; }

  // Must match the breakpoint in site.css.
  var narrowMQ = window.matchMedia("(max-width: 960px)");

  function openSidebar() {
    inner.classList.add("is-open");
    btn.setAttribute("aria-expanded", "true");
  }

  function closeSidebar() {
    inner.classList.remove("is-open");
    btn.setAttribute("aria-expanded", "false");
  }

  btn.addEventListener("click", function () {
    inner.classList.contains("is-open") ? closeSidebar() : openSidebar();
  });

  // Escape closes the sidebar and returns focus to the toggle button,
  // matching the ARIA Authoring Practices Guide disclosure-widget pattern.
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" &&
        inner.classList.contains("is-open") &&
        narrowMQ.matches) {
      closeSidebar();
      btn.focus();
    }
  });

  // When the viewport widens past the breakpoint the sidebar becomes visible
  // via CSS alone.  Clear is-open so the collapsed state does not persist if
  // the viewport is later narrowed again (which would leave aria-expanded
  // incorrectly set to "true" with the panel already open via CSS).
  var mqChangeHandler = function (e) {
    if (!e.matches) { closeSidebar(); }
  };

  if (typeof narrowMQ.addEventListener === "function") {
    narrowMQ.addEventListener("change", mqChangeHandler);
  } else if (typeof narrowMQ.addListener === "function") {
    // Legacy fallback: Safari < 14.
    narrowMQ.addListener(mqChangeHandler);
  }

}());
