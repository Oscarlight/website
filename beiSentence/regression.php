<?php
// reset uploadfile to empty
$_SESSION['uploadfile'] = '';
?>
<div>	
		
	<!-- lite version -->
	<!-- <form enctype="multipart/form-data" name="fileUpload" id="uploadForm" action="jQuery/upload.php" method="POST">
    <input type="hidden" name="MAX_FILE_SIZE" value="512000" />
    Send this file: <input name="userfile" type="file" />
    <input type="submit" value="Send File" />
	</form> -->
	
	<div class="container">
      <div class="panel panel-default">
        <div class="panel-heading"><strong>Upload Files</strong> <small>only csv format</small></div>
        <div class="panel-body">

          <h4>Select Your Data File | 选择你的数据文件 </h4>
          <!-- make sure enctype is the right type and action point to the right php -->
          <form enctype="multipart/form-data" name="fileUpload" id="uploadForm" action="regression/userData.php" method="POST">
            <div class="form-inline">
              <div class="form-group">
                <input type="file" name="userfile" id="userfile" accept = ".csv" />
              </div>
              <button type="submit" class="btn btn-sm btn-primary" id="js-upload-submit">Upload files | 上传 </button>
            </div>
          </form>
	    </div>
      </div>
    </div> 
    <!-- <div>
    	<form id = "FFX" >
    		<button type = "submit" class = "btn btn-info" name = "submit" id = "submit"> FFX Algorithm </button>
    	</form>
    	<form id = "GP" >
    		<button type = "submit" class = "btn btn-info" name = "submit" id = "submit"> Evolution Algorithm </button>
    	</form>
    </div> -->
    <div class="btn-group btn-group-justified" role="group" aria-label="...">
  	<div class="btn-group" role="group">
    <button type="button" class="btn btn-info btn-lg" name = "button1" id = "button1">FFX Algorithm</button>
    <p><i>Based on http://trent.st/ffx/</i></p>
  	</div>
  	<div class="btn-group" role="group">
    <button type="button" class="btn btn-danger btn-lg" name = "button2" id = "button2">Evolution Algorithm</button>
    <p><i>Based on https://github.com/lagodiuk/genetic-algorithm</i></p>
  	</div>
  	<div class="btn-group" role="group">
    <button type="button" class="btn btn-default btn-lg" name = "button3" id = "button3">Stop Evolution</button>
    <p><i> &nbsp  </i></p>
  	</div>
	</div>


	<div class="input-group"> &nbsp; </div> <!-- a empty line -->
	<!-- massege -->
	<div class = "input-group" id = "msgReg"></div>

	<!-- results -->
	<div id = "regressionResult"></div>

		
</div>