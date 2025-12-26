let count = 0;
const countEl = document.getElementById("count");

document.getElementById("add").onclick = function () {
  count++;
  countEl.textContent = count;
};

document.getElementById("reset").onclick = function () {
  count = 0;
  countEl.textContent = count;
};

document.getElementById("minus").onclick = function () {
  count--;
  countEl.textContent = count;
};

document.getElementById("theme").onclick = function () {
  document.body.style.background = "#222";
  document.body.style.color = "#fff";
};
