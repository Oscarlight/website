<?php
# debugging
error_reporting(E_ALL);
ini_set("display_errors", "on");

// you can only use $_SESSION['user'] after session_start()
session_start();
// get $dbc to connect to data base
include('../config/connection.php');
// get data_user() function to return user information
include('../functions/data.php');
$user = data_user($dbc, $_SESSION['user']);

$uploaddir = '/var/www/html/upload/';
// !!! the input name in $_FILE['...'] has to be the same !!!
// append user_id to it
// demo mode
if ($_FILES['userfile']['name'] == "") {
	$originfile = "RTD.csv";
} else {
	$originfile = basename($_FILES['userfile']['name']);
}
$newfilename = $user['id'].'_'.$originfile;
$uploadfile = $uploaddir.$newfilename;
$_SESSION['uploadfile'] = $newfilename;
// $sucess = '<div class="alert alert-info" role="alert">'."File is valid, and was successfully uploaded.| 上传成功\n".'</div>';
// $fail = '<div class="alert alert-info" role="alert">'."Upload failed | 上传失败".'</div>';
$success = "File is valid, and was successfully uploaded";
$fail = "Upload failed";
if (move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile)) {
   echo "<script type='text/javascript'>alert('$success');</script>";
} else {
   echo "<script type='text/javascript'>alert('$fail');</script>";
   // echo $_POST['input'];
   // echo implode($_FILES)."haah"; // debug
}
?> 