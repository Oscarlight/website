	<?php
		// $shortname = basename($_FILES['userfile']['name']);
		// $filename = "/var/www/html/upload/".$shortname;
		// echo $filename;
		# debugging
		# error_reporting(E_ALL);
		# ini_set("display_errors", "on");
		
		## execute python
    	// use full path on python and .py file
		// set .py to executable by chmod +x .py (not necessary)
		// use exec() instead of shell_exec()
		// must return as json using json.dumps()
		session_start();
		$uploadname = $_SESSION['uploadfile'];
		if ($uploadname == '') {
			echo "<script type='text/javascript'>alert('You have to upload a file first!');</script>";
		} else {
		$filename = "/var/www/html/upload/".$uploadname;
		$target = "/home/oscar/Documents/AptanaStudio3Workspace/ffxREMOTERUN/".$uploadname;
		$cmd = "python3.5 -S -W ignore /home/oscar/Documents/AptanaStudio3Workspace/ffxREMOTERUN/run.py ".$target;
		// $cmd = "rm figure_1.png";
		include('../functions/ssh.php');

		// $output = sshSimpleRemote($cmd);
		$output = sshRemote($filename, $target, $cmd);
		$oArray = json_decode($output);
		$display = "";
		$length = count($oArray);
		for ($i = 0; $i < $length; $i++) {
			// add to display, not the last one
			$display = $display.$oArray[$i];
		}
		# check the user and origin input
		// $whoami = exec("whoami");
		// echo $whoami;
		// echo $parse;
		
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
