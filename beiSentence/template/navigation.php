		<nav class = "navbar navbar-default" role = "navigation" >

			<div class = "container">
				<ul class = "nav navbar-nav">
					
					<!-- creating a Dynamic navigation / memu: Part 13 -->
					<!-- here I use URL to load content with $_GET -->
					
					<li<?php if($pageid == 1) { echo ' class="active"';} ?>>
						<a href="?page=1"> <div align="center"> Home Page <br> 主页 </div> </a>
					</li>
					<li<?php if($pageid == 6) { echo ' class="active"';} ?>>
						<a href="?page=6"> <div align="center"> Bei Sentence Analyser <br> 被字句分析 </div> </a>
					</li>
					<li<?php if($pageid == 7) { echo ' class="active"';} ?>>
						<a href="?page=7"> <div align="center"> Physics-Inpired Neural Network <br> “悟”理神经网络 </div> </a>
					</li>
					<li<?php if($pageid == 9) { echo ' class="active"';} ?>>
						<a href="?page=9"> <div align="center"> Symbolic Regression <br> 符号回归 </div> </a>
					</li>
					<li<?php if($pageid == 10) { echo ' class="active"';} ?>>
						<a href="?page=10"> <div align="center"> Device Simulator <br> 器件仿真 </div> </a>
					</li>
					<li<?php if($pageid == 5) { echo ' class="active"';} ?>>
						<a href="?page=5"> <div align="center"> About Me <br> 关于我 </div> </a>
					</li>

					
						<ul class = "nav navbar-nav navbar-right">
							<li class = "dropdown">
								<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
									<?php echo ' '.$user['fullname']; ?> 
									<span class="caret"></span>
								</a>
								<ul class="dropdown-menu">
									<li>
										<a href="login/logout.php"> Log Out | 退出 </a>
									</li>
								</ul>
							</li>

						</ul>
				</ul>
			</div>
		</nav><!-- END Main navigation -->
