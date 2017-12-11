	<?php
		# Debugging
		error_reporting(E_ALL);
		ini_set("display_errors", "on");
		
		session_start();
		$uploadname = $_SESSION['uploadfile'];
		if ($uploadname == '') {
			echo "<script type='text/javascript'>alert('You have to upload a file first!');</script>";
		} 
		else {
		$target = "/var/www/html/upload/".$uploadname."_out";
		$filename = "/home/oscar/Documents/AptanaStudio3Workspace/ffxREMOTERUN/".$uploadname."_out";
		// $cmd = "rm figure_1.png";
		include('../functions/ssh.php');
		// just copy
		//!!!!!!!! Comment Just for demo
		sshReceive($filename, $target);
		// read the file
		$myfile = fopen($target, "r") or die("Unable to open file!");
		$display = fread($myfile,filesize($target));
		fclose($myfile);
		
		# echo to format html to display $result
		$html =  '
		<div class="panel panel-default">
    		<div class="panel-heading">
    			<h3 class="panel-title"> Results: </h3>
  			</div>
  			<div class="panel-body">
  			<pre>'.
    	    $display
  		   .'</pre>
  			</div>
		</div>';
		
		# for test only	
		// $finalResult = '<div class="alert alert-info" role="alert">'.'Haha'.'</div>';	
		// $returnArray = array($html);
		
		// echo json_encode($returnArray);
		echo $html;
		// echo $length;
		}
	
	?>
