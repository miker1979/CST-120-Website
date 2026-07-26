document.addEventListener("DOMContentLoaded", function () {
  const year = new Date().getFullYear();

  document.querySelectorAll(".current-year").forEach(function (yearElement) {
    yearElement.textContent = year;
  });

  const copyrightElement = document.getElementById("copyright");

  if (copyrightElement) {
    copyrightElement.innerHTML =
      `&copy; ${year} Ghostline Technology LLC. All rights reserved.`;
  }
});
