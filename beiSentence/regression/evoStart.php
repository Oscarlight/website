	<?php
		// $shortname = basename($_FILES['userfile']['name']);
		// $filename = "/var/www/html/upload/".$shortname;
		// echo $filename;
		# debugging
		error_reporting(E_ALL);
		ini_set("display_errors", "on");
		
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
		$cmd = "java -jar /home/oscar/Documents/AptanaStudio3Workspace/ffxREMOTERUN/evo.jar ".$target." 100";
		// $cmd = "rm figure_1.png";
		include('../functions/ssh.php');

		sshRemote($filename, $target, $cmd);

		
		# echo to format html to display $result
		$html =  '
		<div class="panel panel-default">
    		<div class="panel-heading">
    			<h3 class="panel-title"> Results: </h3>
  			</div>
  			<div class="panel-body">
  			<pre>'.
    	    "A new evolution is started..."
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
