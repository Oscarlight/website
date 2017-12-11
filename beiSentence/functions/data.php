<?php

function data_page($dbc, $pageid) {
    // run the query 
	$query = "SELECT * FROM pages WHERE id = $pageid"; // use double quote
	/*
	 * 1: store the data into the result variable which is a
	 * mysql object,
	 * 2: convert mysql object to an associated (i.e. use words as
	 * the key) array (instead of using numerical array)
	 */
	
    $dbc->set_charset("utf8"); // Set UTF-8 as the default character set for all MySQL connections
	$result = mysqli_query($dbc, $query);
	$page = mysqli_fetch_assoc($result);
	return $page; 
} 

/* read user info */
function data_user($dbc, $id) {
	$q = "SELECT * FROM users WHERE email = '$id'";
	$r = mysqli_query($dbc, $q);
	$user = mysqli_fetch_assoc($r);
	$user['fullname'] = $user['first'].' '.$user['last'];
	return $user;
}
 
?>