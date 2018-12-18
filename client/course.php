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
  <title>Course</title>
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/datatables/data-tables.bootstrap4.min.css">
  <link rel="stylesheet" href="assets/socicon/css/styles.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="stylesheet" href="assets/extra/css/extra.css">
  

  <script src="assets/jquery/jquery.min.js"></script>
  <script src="assets/popper/popper.min.js"></script>
  <script src="assets/tether/tether.min.js"></script>
  <script src="assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="assets/smoothscroll/smooth-scroll.js"></script>
  <script src="assets/dropdown/js/script.min.js"></script>
  <script src="assets/touchswipe/jquery.touch-swipe.min.js"></script>
  <script src="assets/theme/js/script.js"></script>
  
  <?php
		$continue = false;
		if ((isset($_SESSION['teacher'])) && ($_SESSION['teacher'] == 1)) {
			global $conn;
			$sth = $conn->query("SELECT * FROM courses WHERE course_id='".$_GET['id']."'");
			$result = $sth->fetch();
			if (!is_array($result)) {
				echo("The course ID does not exist.");
			}
			else {
				$teachers = getCourseTeachers($result['course_id']);
			}
			foreach ($teachers as $teacher) {
				if ($teacher['id'] == $_SESSION['id']) {
					$continue = true;
				}
			}
		}
		
		if ($continue == true) {
			$_SESSION['continue'] = 1;
			
	?>
	<script type="text/javascript">
		$(document).ready(function () {
			function showResult() {
			  if ($("#search").val() == 0) { 
				document.getElementById("searchResults").innerHTML="";
				document.getElementById("searchResults").style.border="0px";
				return;
			  }
			  if (window.XMLHttpRequest) {
				xmlhttp=new XMLHttpRequest();
			  }
			  else {
				xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
			  }
			  xmlhttp.onreadystatechange=function() {
				if (this.readyState==4 && this.status==200) {
				  document.getElementById("searchResults").innerHTML=this.responseText;
				  document.getElementById("searchResults").style.border="1px solid #2E2E2E";
				}
			  }
			  xmlhttp.open("GET", "search.php?q="+$("#search").val()+"&c=<?php echo($_GET['id']); ?>",true);
			  xmlhttp.send();
			}
			document.getElementById ("search").addEventListener("keyup", showResult, false);
		});
		//window.addEventListener('beforeunload', function(e) {
		//	<?php
		//		unset($_SESSION['continue']);
		//	?>
		//});
	</script>
	<?php
		}
	?>
</head>
<body>
  <?php
  include('includes/header.php');
  ?>
<section class="mbr-section content4 cid-rbRivNiOjv">
    <div class="container">
        <div class="media-container-row row justify-content-center">
			<?php
				if (!isset($_GET['id'])) {
					echo("No course ID specified.");
				}
				else {
					global $conn;
					$sth = $conn->query("SELECT * FROM courses WHERE course_id='".$_GET['id']."'");
					$result = $sth->fetch();
					if (!is_array($result)) {
						echo("The course ID does not exist.");
					}
					else {
						echo("<h1>".$result['name']."</h1>");
						$teachers = getCourseTeachers($result['course_id']);
						echo("<h2>Professors: ");
						$count = 0;
						foreach($teachers as $teacher) {
							$count++;
							echo("<a href=\"profile.php?id=".$teacher['id']."\">".$teacher['name']."</a>, ".$teacher['email']);
							if ($count < count($teachers)) {
								echo(" | ");
							}
						}
						echo("</h2>");
						$students = getStudentsEnrolled($result['course_id']);
						echo("<table>");
						foreach ($students as $student) {
							echo("<tr><td align=\"left\"><a href=\"profile.php?id=".$student['id']."\">".$student['name']."</a></td><td align=\"center\">".$student['email']."</td><td align=\"right\"><a href=\"drop_from_course.php?cid=".$_GET['id']."&id=".$student['id']."\">x</a></td></tr>");
						}
						echo("</table>");
					}
				}
			?>
		</div>
	</div>
</section>

<?php
	if ($continue == true) { ?>
<div align="center">
<?php if (isset($_GET['s'])) { ?> Student successfully added. <?php }
else if (isset($_GET['r'])) { ?> Student successfully dropped. <?php } ?>
<form>
	<input id="search" type="text" size="30">
	<div id="searchResults"></div>
</form></div>
<?php } /*

	
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
*/
?>
  
  
</body>
</html>