<?php
	include('includes/database.php');
	include('includes/session.php');
	include('includes/functions.php');
?>
<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <meta name="description" content="">
  <title>Profile</title>
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/datatables/data-tables.bootstrap4.min.css">
  <link rel="stylesheet" href="assets/socicon/css/styles.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="stylesheet" href="assets/extra/css/extra.css">
  
  
  
</head>
<body>
  <?php
  include('includes/header.php');
  ?>
<section class="mbr-section content4 cid-rbRivNiOjv">
    <div class="container">
        <div class="media-container-row row justify-content-center">
			<?php
				if (!isset($_GET['id']) && !isset($_SESSION['login'])) {
					echo("You are not logged in and did not specify a user ID.");
				}
				else if (isset($_GET['id'])) {
					global $conn;
					$sth = $conn->query("SELECT * FROM accounts WHERE id='".$_GET['id']."'");
					$result = $sth->fetch();
					if (!is_array($result)) {
						echo("The user ID does not exist.");
					}
					else {
						echo("<table width=\"50%\">");
						echo("<tr><td align=\"left\">".$result['name']."</td><td align=\"right\">".$result['email']."</td></tr>");
						echo("<tr>");
						$courses = getAccountCourses($result['id']);
						foreach ($courses as $course) {
							echo("<tr><td align=\"left\"><a href=\"course.php?id=".$course['course_id']."\">".$course['name']."</a></td><td align=\"center\">".$course['location']."</td><td align=\"right\">");
							$teachers = getCourseTeachers($course['course_id']);
							$count = 0;
							foreach($teachers as $teacher) {
								$count++;
								echo("<a href=\"profile.php?id=".$teacher['id']."\">".$teacher['name']."</a>, ".$teacher['email']);
								if ($count < count($teachers)) {
									echo(" | ");
								}
							}
							echo("</td></tr>");
						}
						echo("</table>");
					}
				}
				else if (isset($_SESSION['login'])) {
					$sth = $conn->query("SELECT * FROM accounts WHERE id='".$_SESSION['id']."'");
					$result = $sth->fetch();
					if (!is_array($result)) {
						echo("This person is not enrolled in any courses.");
					}
					else {
						echo("<table width=\"50%\">");
						echo("<tr><td align=\"left\">".$result['name']."</td><td align=\"center\">&nbsp;</td><td align=\"right\">".$result['email']."</td></tr>");
						echo("<tr>");
						$courses = getAccountCourses($result['id']);
						foreach ($courses as $course) {
							echo("<tr><td align=\"left\"><a href=\"course.php?id=".$course['course_id']."\">".$course['name']."</a></td><td align=\"center\">".$course['location']."</td><td align=\"right\">");
							$teachers = getCourseTeachers($course['course_id']);
							$count = 0;
							foreach($teachers as $teacher) {
								$count++;
								echo("<a href=\"profile.php?id=".$teacher['id']."\">".$teacher['name']."</a>, ".$teacher['email']);
								if ($count < count($teachers)) {
									echo(" | ");
								}
							}
							echo("</td></tr>");
						}
						echo("</table>");
					}
				}
			?>
		</div>
	</div>
</section>
	
<section once="" class="cid-rbPWu4zeDY" id="footer7-b">

    

    

    <div class="container">
        <div class="media-container-row align-center mbr-white">
            <div class="row row-links">
                <ul class="foot-menu">
                    
                    
                    
                    
                    
                <li class="foot-menu-item mbr-fonts-style display-7">
                        <a class="text-white mbr-bold" href="about.php"><strong>About AutoGrader</strong></a></li><li class="foot-menu-item mbr-fonts-style display-7"><a class="text-white mbr-bold" href="http://nyu.edu"><strong>NYU</strong></a></li></ul>
            </div>
            <div class="row row-copirayt">
                <p class="mbr-text mb-0 mbr-fonts-style mbr-white align-center display-7"></p>
            </div>
        </div>
    </div>
</section>


  <script src="assets/jquery/jquery.min.js"></script>
  <script src="assets/popper/popper.min.js"></script>
  <script src="assets/tether/tether.min.js"></script>
  <script src="assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="assets/smoothscroll/smooth-scroll.js"></script>
  <script src="assets/dropdown/js/script.min.js"></script>
  <script src="assets/touchswipe/jquery.touch-swipe.min.js"></script>
  <script src="assets/theme/js/script.js"></script>
  
  
</body>
</html>