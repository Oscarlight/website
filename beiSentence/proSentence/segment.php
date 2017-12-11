	<?php
		// store input sentence
		$sentence = trim($_POST['input']);
		
		### give and ONLY need to give temp.txt group write permisson chmod 0666 temp.txt
		$filename = "/var/www/html/tempForSSH/segment.txt";
		file_put_contents($filename, $sentence);
		
		# Debugging
		error_reporting(E_ALL);
		ini_set("display_errors", "on");
		
		$target = "/home/oscar/Documents/AptanaStudio3Workspace/segmenterREMOTERUN/temp.txt";
		$cmd = "bash /home/oscar/Documents/AptanaStudio3Workspace/segmenterREMOTERUN/segment.sh ctb ".$target." UTF-8 0";
		include('../functions/ssh.php');
		$data = sshRemote($filename, $target, $cmd);
				
		# format html to display $result
		$html = '
		<div class="panel panel-default">
    		<div class="panel-heading">
    			<h3 class="panel-title"> 句子分词 | Segmentation </h3>
  			</div>
  			<div class="panel-body">
  			<pre>'.
    	    $data
  		   .'</pre>
  		    <p><i>
  		    Huihsin Tseng, Pichuan Chang, Galen Andrew, Daniel Jurafsky and Christopher Manning. 2005. A Conditional Random Field Word Segmenter. In Fourth SIGHAN Workshop on Chinese Language Processing.
  		    </i></p>
  			</div>
		</div>
		';
		
		$parsingWait = '<div class="alert alert-info" role="alert"> 
				计算句子解析树中。。。 (parsing) </div>';
		
		# put the orginal data and html form into an array
		$returnArray = array($html, $data, $parsingWait);
		
		# echo back to jQuery by using json_encode to a javaScript variable
		echo json_encode($returnArray);
		
		// echo $data;
	?>