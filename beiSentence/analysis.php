

<div>
	<div>		
	<!-- name, method, action are all for php, here we hijack the php to run jQuery -->
	<!-- <form id = "sentenceInputForm" method = "POST" action = "inSQL.php"> -->
	<!-- javaScript file to handle this submit without refleshing is in config/js.php--->
	<form id = "sentenceInputForm">
		<div class = "form-group">
			<label for = "title"> 请输入被子句 (Enter bei sentence here)：</label>
			<textarea class="form-control" type="text" name="sentence" id="sentence" rows="3">流行歌曲才会被深受大家的喜爱</textarea>
		</div>
		<!-- type is prefixed, you cannot name whatever you want -->
		<button type = "submit" class = "btn btn-info" name = "submit" id = "submit"> 开始分析 | GO! </button>
	</form>
	</div> <!--End Input section-->
	<div class="input-group"> &nbsp; </div> <!-- a empty line -->
	<!-- massege -->
	<div class = "input-group" id = "msg"></div>
	<!-- loading -->
	<div class = "input-group" id = "load"></div>
	<!-- segmentation -->
	<div id = "segment-result"></div>
	<!-- parsing -->
	<div class = "input-group" id = "parsing-wait"></div>
	<!-- parsing-reslut -->
	<div id = "parsing-result"></div>
	<!-- search -->
	<div class = "input-group" id = "processing"></div>
	<div id = "search-result"></div>
	<!-- Final result -->
	<div class = "input-group" id = "result"></div>
		
</div>