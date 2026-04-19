document.addEventListener("DOMContentLoaded", function () {
  const year = new Date().getFullYear();
  const el = document.getElementById("copyright");

  if (el) {
    el.innerHTML = `&copy; ${year} Mike Robinson | Ghostline Logistics Tech LLC`;
  }
});