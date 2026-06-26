const chatButton = document.querySelector(".chat-button");
const chatWindow = document.querySelector(".chat-window");
const chatClose = document.querySelector(".chat-close");

if (chatButton && chatWindow && chatClose) {
  chatButton.addEventListener("click", () => chatWindow.classList.toggle("active"));
  chatClose.addEventListener("click", () => chatWindow.classList.remove("active"));
  setTimeout(() => chatWindow.classList.add("active"), 2500);
}
