<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="public/style.css">
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form action="auth/login.php" method="post">
            <input type="email" name="email" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <p>Don't have an account? <a href="auth/register.php">Sign Up</a></p>
    </div>
</body>
</html>
