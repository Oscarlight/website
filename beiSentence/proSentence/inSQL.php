	<?php
		// Check if $_POST is set
		if ( empty($_POST['input'] ) ) {
			// echo '<p>亲，不要输入空句子哦。</p>';
			echo '<div class="alert alert-warning" role="alert">亲，不要输入空句子哦。</div>';
			exit;
		}
		
		// Confrim reception
		// echo '<p> 您输入的被句子是: '.$_POST[input].'</p>'
		echo '<div class="alert alert-success" role="alert"> 您输入的被句子是: '.$_POST[input].'</div>';
		
		// Stanford Parsing
		
		
		 
		//TODO： check if has "bei" or "bei" is not 介词
		
		// if(isset($_POST['submitted']) == 1 and $_POST['sentence'] != '') {
			// # Send to MySQL
			// $q = "INSERT INTO analysis (user, sentence) VALUES ('$user[fullname]','$_POST[sentence]')";
			// // use the $user from setup.php
			// $r = mysqli_query($dbc, $q);
			// if($r) { // if $r has value
				// echo '<p>亲，句子已收到。一群猴子在努力分析中...</p>';
// 			
				// # Parser the Sentence
// 				
// 				
			// } else {
				// echo '<p>亲，句子不知道去哪儿了... </p>：'.mysqli_error($dbc);
				// echo '<p>'.$q.'</p>'; // check our query
			// } 
		// } else if(isset($_POST['submitted']) == 1) {
				// echo '<p>亲，不要输入空句子哦。</p>';
		// }
	?>