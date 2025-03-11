document.addEventListener("DOMContentLoaded", function () {
    const chatWindow = document.getElementById("chat-window");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    function appendMessage(sender, message) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add(sender);
        messageDiv.innerText = message;
        chatWindow.appendChild(messageDiv);
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;
        appendMessage("user", message);
        userInput.value = "";
        
        fetch("/api/chatbot/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_input: message })
        })
        .then(response => response.json())
        .then(data => {
            appendMessage("bot", data.message);
            if (data.options.length) {
                appendMessage("bot", "Options: " + data.options.join(", "));
            }
        })
        .catch(error => console.error("Error:", error));
    }

    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") sendMessage();
    });
});
