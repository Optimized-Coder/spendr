menuToggle = document.getElementById("menu-toggle");
mainNav = document.getElementById("main-nav");

menuToggle.addEventListener("click", () => {
  mainNav.classList.toggle("active");
  if (mainNav.classList.contains("active")) {
    mainNav.style.display = "flex";
    mainNav.style.flexDirection = "column";
    mainNav.style.justifyContent = "center";
    mainNav.style.alignItems = "center";
    mainNav.style.padding = "1rem";
    mainNav.style.textAlign = "center";
  } else {
    mainNav.style.display = "none";
  }
});
