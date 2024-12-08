async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    // Display user message
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="message user"><strong>You:</strong> ${userInput}</div>`;

    // Send user message to the server
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    });
    const data = await response.json();

    // Display assistant response
    if (data.response) {
        chatBox.innerHTML += `<div class="message assistant"><strong>ShopBot:</strong> ${data.response}</div>`;
    }

    // Clear input
    document.getElementById("user-input").value = "";

    // Scroll chat box to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}
