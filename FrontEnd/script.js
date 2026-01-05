const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");

// GANTI URL INI SAAT DEPLOY
const API_URL = "http://127.0.0.1:8080/chat";



function addMessage(text, sender) {
  const div = document.createElement("div");
  div.className = `message ${sender}`;
  div.innerText = text;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, "user");
  input.value = "";

  fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message })
  })
  .then(res => res.json())
  .then(data => {
    addMessage(data.response, "bot");
  })
  .catch(() => {
    addMessage("Gagal terhubung ke server.", "bot");
  });
}

input.addEventListener("keypress", function(e) {
  if (e.key === "Enter") sendMessage();
});
