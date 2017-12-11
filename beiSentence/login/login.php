<?php 
# Start Session
session_start();

# Only Database Connection
include ('../config/connection.php');

if ($_POST) {
	$q = "SELECT * FROM users WHERE email = '$_POST[email]' AND password = SHA1('$_POST[password]') ";
	$r = mysqli_query($dbc, $q);
	$num = mysqli_num_rows($r);
	// result the number of row we find after running the query
	if ($num == 1) {
		$_SESSION['user'] = $_POST['email'];
		header('Location: ../index.php');
	}
}
?>

<!DOCTYPE html>
<html>
	<head>
		<!-- Support Chinese character model -->
		<meta charset="utf-8">

		<title>Website Login</title>

		<!-- from Bootstrap -->
		<meta name="viewport" content="width=device-width, initial-scale=1">

		<!-- include the css file -->
		<?php
		include ('../config/css.php');
		?>

		<!-- include the javascript file -->
		<?php
		include ('../config/js.php');
		?>
	</head>

	<body>

	<?php // include(D_TEMPLATE.'/navigation.php'); ?>

	<div class="container">

	<div class="row">
	<!-- total 12 -->

	<div class="col-md-4 col-md-offset-4">

	<div class = "panel panel-info">

	<div class="panel-heading">
	<strong>登录 | Log In</strong>
	</div><!-- END panel heading -->
	<?php
	// If the passed email or password are not correct,
	// it will not be redicted to index.php above, so
	// these lines below will displaied.
	if($_POST) {
	echo "Wrong email or passwords";
	}
	?>
	<form action="login.php" method="post">
	<div class="form-group">
	<label for="email"> &nbsp;&nbsp; 邮箱 | Email</label>
	<input type="email" class="form-control" id="email" name="email" placeholder="Email">
	</div>
	<div class="form-group">
	<label for="password"> &nbsp;&nbsp; 密码 | Password</label>
	<input type="password" class="form-control" id="password" name="password" placeholder="Password">
	</div>
	<!--
	<div class="checkbox">
	<label>
	<input type="checkbox">
	Check me out </label>
	</div>
	-->
	<button type="submit" class="btn btn-default">
	登录 | Log In
	</button>
	</form>

	</div><!-- End panel body -->

	</div><!-- End column -->

	</div><!-- End row -->

	</div><!-- End container -->

	<?php
	include ('../template/footer.php');
?>
</html>