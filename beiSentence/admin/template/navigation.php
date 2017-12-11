		<nav class = "navbar navbar-default" role = "navigation" >

			<div class = "container">
				<ul class = "nav navbar-nav">
					
					<!-- creating a Dynamic navigation / memu: Part 13>
					<!-- <?php
						$q = "SELECT * FROM pages";
						$r = mysqli_query($dbc, $q);
					
					
					while($nav = mysqli_fetch_assoc($r)) {
					?>
					<?php }
					?> -->
					
					<li<?php if($pageid == 1) { echo ' class="active"';} ?>>
						<a href="?page=1"> Dashboard </a>
					</li>
					<li<?php if($pageid == 5) { echo ' class="active"';} ?>>
						<a href="?page=5"> Setting </a>
					</li>
					<li>
						<a href="logout.php"> Log Out </a>
					</li>
					<!-- <li class="active">
						<a href="valentineSpecial/val.php"> Surprise me </a>
					</li> -->
				</ul>
			</div>
		</nav><!-- END Main navigation -->