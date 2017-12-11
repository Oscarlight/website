<?php

# Start Session
session_start();

unset($_SESSION['user']); // Delete the username key

// session_destroy(); // This would delete all of the session keys
header('Location: login.php'); // Redirect back to login page

?>