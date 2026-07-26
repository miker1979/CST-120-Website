document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("darkModeToggle");

  if (!toggleButton) return;

  // Apply saved theme on load
  if (localStorage.getItem("ghostlineTheme") === "dark") {
    document.body.classList.add("dark-mode");
    toggleButton.textContent = "Light Mode";
  }

  toggleButton.addEventListener("click", function () {
    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
      localStorage.setItem("ghostlineTheme", "dark");
      toggleButton.textContent = "Light Mode";
    } else {
      localStorage.setItem("ghostlineTheme", "light");
      toggleButton.textContent = "Dark Mode";
    }
  });
});