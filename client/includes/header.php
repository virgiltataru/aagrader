<section class="menu cid-rbPSf58Pl3" once="menu" id="menu1-i" style="margin-bottom:100px">
         <nav class="navbar navbar-expand beta-menu navbar-dropdown align-items-center navbar-fixed-top navbar-toggleable-sm">
            <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
               <div class="hamburger">
                  <span></span>
                  <span></span>
                  <span></span>
                  <span></span>
               </div>
            </button>
            <div class="menu-logo">
               <div class="navbar-brand">
                  <span class="navbar-caption-wrap"><a class="navbar-caption text-white display-4" href="index.php">
                  AutoGrader</a></span>
               </div>
            </div>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
               <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true">
                  <li class="nav-item">
                     <?php
					 if (isset($_SESSION['login'])) {
						 echo("<a class=\"nav-link link text-white display-4\" href=\"profile.php\">Hi, ".$_SESSION['name']."<br></a>");
					 }
					 else {
						 echo("<a class=\"nav-link link text-white display-4\" href=\"login.php\">Login<br></a>");
					 }
					?>
                  </li>
                  <li class="nav-item">
				     <?php
					 if (isset($_SESSION['login'])) {
						 echo("<a class=\"nav-link link text-white display-4\" href=\"logout.php\">Logout<br></a>");
					 }
					 else {
						 echo("<a class=\"nav-link link text-white display-4\" href=\"register.php\">Register<br></a>");
					 }
					?>
                  </li>
               </ul>
            </div>
         </nav>
      </section>