// Vietnamese Library Assistant Chatbot JavaScript
document.addEventListener("DOMContentLoaded", function () {
  const userInput = document.getElementById("user-input");
  const sendButton = document.getElementById("send-button");
  const chatMessages = document.getElementById("chat-messages");

  // Set welcome message time
  const welcomeTime = document.getElementById("welcome-time");
  welcomeTime.textContent = getCurrentTime();

  // Event listeners
  sendButton.addEventListener("click", sendMessage);
  userInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  // Focus on input
  userInput.focus();

  function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Disable input while processing
    setInputState(false);

    // Add user message to chat
    addMessage(message, "user");

    // Clear input
    userInput.value = "";

    // Show typing indicator
    showTypingIndicator();

    // Send to backend
    fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    })
      .then((response) => response.json())
      .then((data) => {
        // Remove typing indicator
        removeTypingIndicator();

        // Add bot response
        addMessage(data.response, "bot", data.timestamp);

        // Re-enable input
        setInputState(true);
        userInput.focus();
      })
      .catch((error) => {
        console.error("Lỗi:", error);
        removeTypingIndicator();
        addMessage("Xin lỗi, tôi gặp lỗi. Vui lòng thử lại.", "bot");
        setInputState(true);
        userInput.focus();
      });
  }

  function addMessage(content, sender, timestamp = null) {
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${sender}-message`;

    const messageContent = document.createElement("div");
    messageContent.className = "message-content";

    if (sender === "user") {
      messageContent.innerHTML = `<strong>Bạn:</strong> ${escapeHtml(content)}`;
    } else {
      messageContent.innerHTML = `<strong>Trợ lý Thư viện:</strong> ${escapeHtml(
        content
      )}`;
    }

    const messageTime = document.createElement("div");
    messageTime.className = "message-time";
    messageTime.textContent = timestamp || getCurrentTime();

    messageDiv.appendChild(messageContent);
    messageDiv.appendChild(messageTime);

    chatMessages.appendChild(messageDiv);
    scrollToBottom();
  }

  function showTypingIndicator() {
    const typingDiv = document.createElement("div");
    typingDiv.className = "message bot-message typing-indicator";
    typingDiv.id = "typing-indicator";

    const typingContent = document.createElement("div");
    typingContent.className = "message-content";
    typingContent.innerHTML = `
            <div class="typing-indicator">
                <span>Trợ lý Thư viện đang nhập</span>
                <div class="typing-dots">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
        `;

    typingDiv.appendChild(typingContent);
    chatMessages.appendChild(typingDiv);
    scrollToBottom();
  }

  function removeTypingIndicator() {
    const typingIndicator = document.getElementById("typing-indicator");
    if (typingIndicator) {
      typingIndicator.remove();
    }
  }

  function setInputState(enabled) {
    userInput.disabled = !enabled;
    sendButton.disabled = !enabled;
    if (enabled) {
      sendButton.textContent = "Gửi";
    } else {
      sendButton.textContent = "Đang gửi...";
    }
  }

  function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  }

  function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }
});

// Quick message functions (called from HTML)
function sendQuickMessage(message) {
  const userInput = document.getElementById("user-input");
  userInput.value = message;

  // Trigger send
  const sendButton = document.getElementById("send-button");
  sendButton.click();
}

function showHelp() {
  fetch("/help")
    .then((response) => response.json())
    .then((data) => {
      const chatMessages = document.getElementById("chat-messages");
      const messageDiv = document.createElement("div");
      messageDiv.className = "message bot-message";

      const messageContent = document.createElement("div");
      messageContent.className = "message-content";
      messageContent.innerHTML = `<strong>Trợ lý Thư viện:</strong> ${data.response.replace(
        /\n/g,
        "<br>"
      )}`;

      const messageTime = document.createElement("div");
      messageTime.className = "message-time";
      messageTime.textContent = data.timestamp;

      messageDiv.appendChild(messageContent);
      messageDiv.appendChild(messageTime);

      chatMessages.appendChild(messageDiv);
      chatMessages.scrollTop = chatMessages.scrollHeight;
    })
    .catch((error) => {
      console.error("Lỗi khi lấy trợ giúp:", error);
    });
}

// Easter egg: Show rules in console for debugging
console.log("🤖 Trợ lý Thư viện Tiếng Việt đã tải!");
console.log("💡 Mẹo: Thử nhập câu hỏi về giờ mở cửa, sách, phòng học, v.v.");
console.log("🐛 Debug: Truy cập /rules để xem tất cả quy tắc có sẵn");
