document.addEventListener("DOMContentLoaded", function () {
  const toc = document.getElementById("toc-list");
  const empty = document.getElementById("toc-empty");
  const content = document.querySelector(".doc-content");
  if (!toc || !empty || !content) return;

  if (toc.children.length > 0) {
    empty.hidden = true;
    return;
  }

  const headings = content.querySelectorAll("h2[id]");
  // Retain second-level heading support for easy restoration later.
  // const headings = content.querySelectorAll("h2[id], h3[id]");

  headings.forEach(function (h) {
    const li = document.createElement("li");
    // if (h.tagName.toLowerCase() === "h3") li.className = "toc-h3";
    const a = document.createElement("a");
    a.href = "#" + h.id;
    a.textContent = h.textContent;
    li.appendChild(a);
    toc.appendChild(li);
  });

  if (!toc.children.length) {
    empty.hidden = false;
  } else {
    empty.hidden = true;
  }
});