document.getElementById('passwordForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const site = document.getElementById('site').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const passwordList = document.getElementById('passwordList');

    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${site}</td>
        <td>${username}</td>
        <td>${password}</td>
        <td>
            <button onclick="editPassword(this)">Edit</button>
            <button onclick="deletePassword(this)">Delete</button>
        </td>
    `;

    passwordList.appendChild(row);

    // Clear form fields
    document.getElementById('site').value = '';
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
});

function editPassword(button) {
    const row = button.parentElement.parentElement;
    const site = row.cells[0].textContent;
    const username = row.cells[1].textContent;
    const password = row.cells[2].textContent;

    document.getElementById('site').value = site;
    document.getElementById('username').value = username;
    document.getElementById('password').value = password;

    row.remove();
}

function deletePassword(button) {
    button.parentElement.parentElement.remove();
}
