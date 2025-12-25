let count = 0;
const countEl = document.getElementById("count");

document.getElementById("add").onclick = function () {
  count+=2;
  countEl.textContent = count;
};

document.getElementById("reset").onclick = function () {
  count = 0;
  countEl.textContent = count;
};
