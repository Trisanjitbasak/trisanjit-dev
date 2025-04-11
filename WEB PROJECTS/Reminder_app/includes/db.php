<?php
$host = "localhost"; // Change if using an external DB
$user = "root";      // Your DB username
$pass = "";          // Your DB password
$dbname = "reminder_app"; // Your database name

$conn = new mysqli($host, $user, $pass, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
