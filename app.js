async function ask() {
  const query = document.getElementById("query").value;
  if (!query) return;

  // Display user message
  const chatLog = document.getElementById("chat-log");
  const userMsg = document.createElement("div");
  userMsg.className = "message user";
  userMsg.innerText = query;
  chatLog.appendChild(userMsg);

  // Call FastAPI backend
  const res = await fetch(`/ask?query=${encodeURIComponent(query)}`);
  const data = await res.json();

  // Display bot answer
  const botMsg = document.createElement("div");
  botMsg.className = "message bot";
  botMsg.innerText = data.answer;
  chatLog.appendChild(botMsg);

  // Scroll to bottom
  chatLog.scrollTop = chatLog.scrollHeight;

  // Clear input
  document.getElementById("query").value = "";
}
