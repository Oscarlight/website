<?php
	# Start the session
	# if the user is not set, go to login.php
	session_start();
	if (!isset($_SESSION['user'])) {
		header('Location: login.php');
	}
?>




<?php 
	include('config/setup.php'); 
?>


<!DOCTYPE html>
<html>
	<head>
		<!-- Support Chinese character model -->
		<meta charset="utf-8"> 
		
		<title> <?php echo $page['title'].' | Admin' ?> </title>
		
		<!-- from Bootstrap -->
		<meta name="viewport" content="width=device-width, initial-scale=1">
		
		<!-- include the css file -->
		<?php include('config/css.php'); ?>
		
		<!-- include the javascript file -->
		<?php include('config/js.php'); ?>


	</head>

	<body>

		<?php include(D_TEMPLATE.'/navigation.php'); ?>

		
		<?php include(D_TEMPLATE.'/footer.php'); ?>
		
</html>