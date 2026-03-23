document.addEventListener("DOMContentLoaded", function () {
  const year = new Date().getFullYear();
  document.getElementById("copyright").innerHTML =
    "&copy; " + year + " Mike Robinson. All rights reserved.";
});