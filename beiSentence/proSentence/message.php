	<?php
		// Check if $_POST is set
		if ( empty($_POST['input'] ) ) {
			// echo '<p>亲，不要输入空句子哦。</p>';
			echo '<div class="alert alert-warning" role="alert">亲，不要输入空句子哦。(Error: empty sentence) </div>';
			exit;
		}
		
		$sentence = trim($_POST['input']);
		
		// Confrim reception
		// echo '<p> 您输入的被句子是: '.$_POST[input].'</p>'
		$confrim = '<div class="alert alert-success" role="alert"> 您输入的句子是(You entered): '.$sentence.'</div>';
		
		// Confirm it is a sentence with bei
		// use === instead of ==
		if (strpos($_POST[input], '被') === false) {
    		$confrim .= '<div class="alert alert-warning" role="alert"> 您输入的句子里不含有“被”字，目前我只分析含有“被”的被字句
    		(For now, I only analyse the sentence containing "bei")</div>';;
		}
		
		$load = '<div class="alert alert-info" role="alert"> 
				读入中文语料库中，要等几秒哦。。。 (Please wait several seconds for loading Chinese Treebank) </div>';
				
		# put the orginal data and html form into an array
		$returnArray = array($confrim, $load);
		
		# echo back to jQuery by using json_encode to a javaScript variable
		echo json_encode($returnArray);
		
		// echo $confrim;
	?>