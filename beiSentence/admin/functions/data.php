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
	$result = mysqli_query($dbc, $query);
	$page = mysqli_fetch_assoc($result);
	
	return $page; 
} 

 
?>