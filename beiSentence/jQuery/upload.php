<script>
//REFERENCE: http://www.peachpit.com/articles/article.aspx?p=1766159&seqNum=5
$(document).ready(function() {	
    $(function(){
    	$('#uploadForm').submit(function(){
    		
    		// ---- Alternative: Use a iframe ----
    		// $('<input type="hidden" name="javascript" value="yes" />').appendTo($(this));	
            var iframeName = ('iframeUpload');
            var iframeTemp = $('<iframe name="'+iframeName+'" src="about:blank" />');
            // comment it will display the output in the userData.php to the iframe
            // which is good for debug
            iframeTemp.css('display', 'none');
			$('body').append(iframeTemp);
            /* submit the userData.php */
            $(this).attr({				
                action: 'regression/userData.php',
                method: 'post',
                enctype: 'multipart/form-data',
                encoding: 'multipart/form-data',
                target: iframeName
            });
            // ----------------------------------
            
            // Why the following don't work?
            // Cause: in userData.php, no $_FILES['userfile'] index 
            // $.post("regression/userData.php", function(data) {
            	// $('#msgReg').html(data);
            // })
            // //!! the place of this IMPORTANT, it must be inside submit event!!
			// event.preventDefault();
        });
    });
});
</script>

