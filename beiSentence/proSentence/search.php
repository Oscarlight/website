	<?php
		$parse = trim($_POST['input']);

		# debugging
		error_reporting(E_ALL);
		ini_set("display_errors", "on");
		
		## execute python
    	// use full path on python and .py file
		// set .py to executable by chmod +x .py (not necessary)
		// use exec() instead of shell_exec()
		// must return as json using json.dumps()
		# core sentence
		### ONLY PLACE TO CHANGE FOR V1.0 to V2.0: g.py -> g2.py
		$cmd = "python /home/oscar/Documents/AptanaStudio3Workspace/searchREMOTERUN/g.py \"".$parse."\"";
		include('../functions/ssh.php');
		## testing ssh-seclib (not successful yet)
		// $displayAll = sshPHPSecLib($cmd);
		// $displayAll = 'Lala';
		## end-testing ssh
		$output = sshSimpleRemote($cmd);
		$oArray = json_decode($output);
		$display = "";
		$length = count($oArray);
		for ($i = 0; $i < $length - 1; $i++) {
			// add to display, not the last one
			$display = $display.$oArray[$i];
		}
		
		# (CHANGE for v2) GoogleScraper search
		if($oArray[$length-1] == 'FLAG:TRUE') {
			$cmd = "python3.4 /home/oscar/Documents/AptanaStudio3Workspace/searchREMOTERUN/p.py";
			$display = $display."enter";
			$output = sshSimpleRemote($cmd);
			# $display = $display."leave";
			$oArray = json_decode($output);
			$length = count($oArray);
			for ($i = 0; $i < $length - 1; $i++) {
				// add to display, not the last one
				$display = $display.$oArray[$i];
			}	
		}
		
		$displayAll = $display;
// 
		# check the user and origin input
		// $whoami = exec("whoami");
		// echo $whoami;
		// echo $parse;
		
		# echo to format html to display $result
		$html =  '
		<div class="panel panel-default">
    		<div class="panel-heading">
    			<h3 class="panel-title"> 偏误分析 | Error Analysis </h3>
  			</div>
  			<div class="panel-body">
  			<pre>'.
    	    $displayAll
  		   .'</pre>
  			</div>
		</div>';
		
		$finalResult = '<div class="alert alert-info" role="alert">'.$oArray[$length-1].'</div>';
		# for test only	
		// $finalResult = '<div class="alert alert-info" role="alert">'.'Haha'.'</div>';	
		$returnArray = array($html, $finalResult);
		
		echo json_encode($returnArray);
	
	?>