<?php
	# Start the session
	# if the user is not set, go to login.php
	session_start();
	if (!isset($_SESSION['user'])) {
		header('Location: login/login.php');
	}
?>

<?php 
	include('config/setup.php'); 
?>


<!DOCTYPE html>
<html>
	<head>
		<!-- Chinese character model -->
		<meta charset="utf-8"> 
		
		<title> <?php echo $page['title'].' | '.$site_title ?> </title>
		
		<!-- from Bootstrap -->
		<meta name="viewport" content="width=device-width, initial-scale=1">
		
		<!-- include the css file -->
		<?php include('config/css.php'); ?>
		
		<!-- include the javascript file -->
		<?php include('config/js.php'); ?>
		
		<!-- Custom javaScript file: submit without refreshing -->
		<?php if($pageid == 6) {
			include('jQuery/submit.php');
		} ?>
				
		<!-- THIS CODE HAVE to be put here, put in regression.php won't work!! --->		
		<?php if($pageid == 9) {
			include('jQuery/upload.php'); // upload file
			include('jQuery/regress.php');// run regress }
		} ?>
		
	</head>

	<body>

		<?php include('template/navigation.php'); ?>
		<?php include('template/footer.php'); ?>

		<div class = "container">
			<?php if($pageid == 1) { include('template/jumbotron.php');} ?>				

			<?php if($pageid == 5 ) { include('template/regularHeadBody.php');} ?>
			
			<?php if($pageid == 6) { include('template/regularHeadBody.php'); 
			                         include('analysis.php');} ?> <!-- if on analysis page, add its own php -->
			                         
			<?php if($pageid == 7 ) { include('template/regularHeadBody.php');} ?>
			
			<?php if($pageid == 9 ) { include('template/regularHeadBody.php');
									  include('regression.php');} ?>
			<?php if($pageid == 10 ) { include('template/regularHeadBody.php');
									  include('leno.php');} ?>
			
		</div>
		
		
</html>