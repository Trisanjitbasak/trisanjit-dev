function sendMessage() {
    const inputBox = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const userMessage = inputBox.value;

    if (userMessage.trim() === "") {
        return;
    }

    const userHtml = `<div class="user-message"><strong>You:</strong> ${userMessage}</div>`;
    chatBox.innerHTML += userHtml;
    inputBox.value = "";

    fetchChatbotResponse(userMessage);
}

function fetchChatbotResponse(userMessage) {
    // Placeholder for actual API call to Blackbox AI
    // This would typically involve an AJAX request to a server endpoint

    const fakeResponse = "This is a response from Blackbox AI.";

    const botHtml = `<div class="bot-message"><strong>Bot:</strong> ${fakeResponse}</div>`;
    document.getElementById('chat-box').innerHTML += botHtml;
}

function fetchChatbotResponse(userMessage) {
    fetch('https://your-backend-endpoint.com/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
    })
    .then(response => response.json())
    .then(data => {
        const botHtml = `<div class="bot-message"><strong>Bot:</strong> ${data.response}</div>`;
        document.getElementById('chat-box').innerHTML += botHtml;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
    