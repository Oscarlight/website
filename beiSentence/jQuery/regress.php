    <script>
    
    // Very useful function to keep updating stuff.

    $('#msgReg').html("");
	$(document).ready( function(){
        $("#button1").click( function()
           {
           	$('#msgReg').html('<div class="alert alert-success" role="alert"> FFX Algorithm is running... </div>');
			$('#regressionResult').html("");
				$.post('regression/ffx.php', function(data) {
					// var array = JSON.parse(data);
					$('#msgReg').html("");
					$('#regressionResult').html(data);	
				});
           }
        );
        $("#button2").click( function()
           {
           	$('#msgReg').html('<div class="alert alert-success" role="alert"> Evolution Algorithm is starting... </div>');
           	$('#regressionResult').html("");
           	var lineCount = 0;
           	// Start the program
           	// $.post('regression/evoStart.php', function(data) {$('#regressionResult').html(data."ha");});
           	
           	var timeout = setTimeout(
        		$.post('regression/evo.php', {input : lineCount}, function(data) {
					// var array = JSON.parse(data);
					$('#regressionResult').html(data);	
					}), 5000);	
			    $('#msgReg').html("");
           }
        );
        $("#button3").click( function()
           {
           	$('#msgReg').html('<div class="alert alert-success" role="alert"> Evolution Algorithm is stopped </div>');
			clearTimeout(timeout);
           }
        );
        
      }
    )
    </script>