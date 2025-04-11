<?php
session_start();
include '../includes/db.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Fetch user
    $stmt = $conn->prepare("SELECT id, password FROM users WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows == 1) {
        $user = $result->fetch_assoc();
        
        // Verify password
        if (password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];

            // Store login info
            $ip = $_SERVER['REMOTE_ADDR'];
            $user_agent = $_SERVER['HTTP_USER_AGENT'];
            $stmt = $conn->prepare("INSERT INTO logins (user_id, ip_address, user_agent) VALUES (?, ?, ?)");
            $stmt->bind_param("iss", $user['id'], $ip, $user_agent);
            $stmt->execute();

            // Redirect to dashboard
            header("Location: ../dashboard/index.php");
            exit();
        } else {
            echo "Invalid password!";
        }
    } else {
        echo "User not found!";
    }
}
?>
