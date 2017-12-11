	<?php
		// store input sentence
		$sentence = $_POST['input'];
		
		
		### give and ONLY need to give temp.txt group write permisson chmod 0666 temp.txt
		$filename = "/var/www/html/tempForSSH/parse.txt";
		file_put_contents($filename, $sentence);
		
		# Debugging
		error_reporting(E_ALL);
		ini_set("display_errors", "on");
		
		$target = "/home/oscar/Documents/AptanaStudio3Workspace/parserREMOTERUN/temp.txt";
		$cmd = "bash /home/oscar/Documents/AptanaStudio3Workspace/parserREMOTERUN/lexparser.sh ".$target;
		include('../functions/ssh.php');
		$output = sshRemote($filename, $target, $cmd);
  
		# format html to display $result
		$html = '
		<div class="panel panel-default">
    		<div class="panel-heading">
    			<h3 class="panel-title"> 句子解析 | Parsing </h3>
  			</div>
  			<div class="panel-body">
  			<pre>'.
    	    $output
  		   .'</pre>
  		    <p>
  		    Using Penn Chinese Treebank (http://www.cis.upenn.edu/~chinese/)</p>
  		    <p><i>
  		    Roger Levy and Christopher D. Manning. 2003. Is it harder to parse Chinese, or the Chinese Treebank? ACL 2003, pp. 439-446.
  		    </i></p>
  			</div>
		</div>
		';
		
		$analyzing = '<div class="alert alert-info" role="alert"> 
				偏误分析中。。。 (analyzing ... sorry for the wait ...) </div>';
		# put the orginal data and html form into an array
		$returnArray = array($html, $output, $analyzing);
		
		# echo back to jQuery by using json_encode to a javaScript variable
		echo json_encode($returnArray);
	
	?>