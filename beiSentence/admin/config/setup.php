<?php

	# Database Connection
	include('../config/connection.php');
	
	# Constants:
	DEFINE('D_TEMPLATE', 'template'); // dirctery of template
	
    // set up varables
	$site_title = 'Jiayan Thesis';
	
	# Functions
	include('functions/data.php');
	
	/* is there a page variable in url, display that page,
	 * if not display page=1 (home page)
	 */ 
	if(isset($_GET['page'])) {
		$pageid = $_GET['page'];
	} else {
		$pageid = 1;
	}

	# Page setup
	$page = data_page($dbc,$pageid);	
	
?>