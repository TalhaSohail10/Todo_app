// Get saved theme from localStorage
const savedTheme = localStorage.getItem("theme") || "light";
document.documentElement.setAttribute("data-theme", savedTheme);
document.getElementById("theme-toggle").textContent = savedTheme === "dark" ? "☀️ Light" : "🌙 Dark";

// Toggle theme on button click
document.getElementById("theme-toggle").addEventListener("click", function () {
    let currentTheme = document.documentElement.getAttribute("data-theme");
    let newTheme = currentTheme === "light" ? "dark" : "light";

    document.documentElement.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);

    this.textContent = newTheme === "dark" ? "☀️ Light" : "🌙 Dark";
});
