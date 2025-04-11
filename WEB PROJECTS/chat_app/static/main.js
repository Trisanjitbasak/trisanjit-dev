document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    const messages = document.getElementById('messages');
    const sendButton = document.getElementById('send');
    const usernameInput = document.getElementById('username');
    const messageInput = document.getElementById('message');

    sendButton.addEventListener('click', () => {
        const username = usernameInput.value.trim();
        const message = messageInput.value.trim();

        if (username && message) {
            socket.emit('send_message', { username, message });
            messageInput.value = '';
        }
    });

    socket.on('receive_message', (data) => {
        const p = document.createElement('p');
        p.innerHTML = `<strong>${data.username}:</strong> ${data.message}`;
        messages.appendChild(p);
        messages.scrollTop = messages.scrollHeight;
    });
});
