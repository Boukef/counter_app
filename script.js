let count = 0;

document.getElementById("add").onclick = function () {
  count++;
  document.getElementById("count").textContent = count;
};