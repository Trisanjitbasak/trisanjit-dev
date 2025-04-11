document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const masterPassword = document.getElementById('masterPassword').value;
    
    // Debugging statement
    console.log('Master Password Entered:', masterPassword);
    
    // Here, the master password is hardcoded for simplicity
    // In a real application, you should use a more secure method
    const storedMasterPassword = 'password123';
    
    if (masterPassword === storedMasterPassword) {
        // Redirect to dashboard
        window.location.href = 'dashboard.html';
    } else {
        // Show error message
        document.getElementById('error').style.display = 'block';
    }
});
