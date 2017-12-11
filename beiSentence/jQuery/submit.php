	<!-- submit form without refreshing (using jQuery/AJAX) -->
	
	<script>
	$(document).ready(function(){
		// set form variable
		var form = $('#sentenceInputForm');
		// Hijack form submit
		form.submit(function(event){
			// set sentence variable
			var sentence = $('#sentence').val();
			
			// clear up all the fields
			$('#segment-result').html("");
			$('#parsing-result').html("");
			$('#search-result').html("");
			$('#result').html("");
			
			// process AJAX request
			// trim the input to ignore empty spaces
			if ($.trim(sentence) != '') {
				
				// send sentence in name of "input", do $_POST('input') in php
				/** message **/
				$.post('proSentence/message.php', {input: sentence}, function(data){
					var array = JSON.parse(data);
					$('#msg').html(array[0]);
					$('#load').html(array[1]);
				});

				/** segementation **/
				$.post('proSentence/segment.php', {input: sentence}, function(data){
					$('#load').html(""); // make loading alert disappear
					var array = JSON.parse(data);
					$('#segment-result').html(array[0]);
					$('#parsing-wait').html(array[2]);
				    /** parsing **/
				    $.post('proSentence/parse.php', {input: array[1]}, function(data){
				    	$('#parsing-wait').html(""); 
						var array = JSON.parse(data);
						$('#parsing-result').html(array[0]);
						$('#processing').html(array[2]);
						/** search **/
						$.post('proSentence/search.php', {input: array[1]}, function(data){
							$('#processing').html("");
							var array = JSON.parse(data);
							$('#search-result').html(array[0]);
							$('#result').html(array[1]);
						});
					});
				});
			};
			//!! the place of this IMPORTANT, it must be inside submit event!!
			event.preventDefault();
		});
	});
	</script>