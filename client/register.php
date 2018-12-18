<?php
   include('includes/database.php');
   include('includes/session.php');
	include('includes/functions.php');
   if (isset($_SESSION['login']) && !isset($_GET['r'])) {
     header('LOCATION:index.php');
	 die();
   }
   if (isset($_GET['r']) && isset($_POST['submit'])) {
	    global $conn;
		$email = $_POST['email'];
		$name = $_POST['name'];
		$password = md5($_POST['password']);
		$sth = $conn->query("SELECT * FROM accounts WHERE email='".$email."'");
		$result = $sth->fetch();
		if (is_array($result)) {
			$email_taken = true;
		}
   }
   ?>
<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <meta name="description" content="">
  <title>Register</title>
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/datatables/data-tables.bootstrap4.min.css">
  <link rel="stylesheet" href="assets/socicon/css/styles.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="stylesheet" href="assets/extra/css/extra.css" type="text/css">


  <script src="assets/jquery/jquery.min.js"></script>
  <script src="assets/jquery/jquery.validate.js"></script>
  <script src="assets/popper/popper.min.js"></script>
  <script src="assets/tether/tether.min.js"></script>
  <script src="assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="assets/smoothscroll/smooth-scroll.js"></script>
  <script src="assets/dropdown/js/script.min.js"></script>
  <script src="assets/touchswipe/jquery.touch-swipe.min.js"></script>
  <script src="assets/theme/js/script.js"></script>
  
  <script type="text/javascript">
	$(document).ready(function() {
		
		$('input').on('blur keyup', function() {
			if ($("#registerForm").valid()) {
				$('#registerButton').prop('disabled', false);  
			} else {
				$('#registerButton').prop('disabled', 'disabled');
			}
		});
		
		$("#registerForm").validate({
			rules: {
				email: {
					required: true,
					email: true
				},
				name: {
					required: true,
					minlength: 4
				},
				password: {
					required: true,
					minlength: 6
				}
			}
		});

	});
</script>
</head>
<body>
      <?php
	  include('includes/header.php');
	  ?>

<section class="mbr-section form1 cid-rbPOSs1tum" id="form1-5">

    

    
    <div class="container">
        <div class="row justify-content-center">
            <div class="title col-12 col-lg-8">
                <h2 class="mbr-section-title align-center pb-3 mbr-fonts-style display-2">
                    <br>Register for AutoGrader</h2>
                
            </div>
        </div>
    </div>
    <div class="container">
        <div class="row justify-content-center">
            <?php
				if (!isset($_GET['r']) || isset($email_taken) || !isset($email)) {
			?>
					<div class="media-container-column col-lg-8" data-form-type="formoid">
                    
            
                    <form id="registerForm" class="mbr-form" action="register.php?r=1" method="post">
                            <div class="col-md-4 multi-horizontal" data-for="email">
                                <div class="form-group">
                                    <label class="form-control-label mbr-fonts-style display-7" for="name-form1-5">Email</label>
                                    <input type="text" class="form-control" name="email" data-form-field="Email" required="" id="email">
                                </div>
                            </div>
                            
                            <div class="col-md-4 multi-horizontal" data-for="name">
                                <div class="form-group">
                                    <label class="form-control-label mbr-fonts-style display-7" for="name-form1-5">Name</label>
                                    <input type="text" class="form-control" name="name" data-form-field="Name" id="name">
                                </div>
                            </div>
                        
                            <div class="col-md-4 multi-horizontal" data-for="password">
                                <div class="form-group">
                                    <label class="form-control-label mbr-fonts-style display-7" for="name-form1-5">Password</label>
                                    <input type="password" class="form-control" name="password" data-form-field="Password" id="password">
                                </div>
                            </div>
            
                        <span class="input-group-btn"><button id="registerButton" href="" type="submit" class="btn btn-primary btn-form display-4" name="submit" disabled="disabled">REGISTER</button></span>
                    </form>
            </div>
			<?php
				if (isset($email_taken)) {
					echo("Sorry, that email is already registered. Please try a new one.");
				}
			}
			else if (isset($_POST['submit'])) {
					$conn->prepare("INSERT INTO accounts (email, password, name) VALUES (?, ?, ?)")->execute([$email, $password, $name]);
					echo("Thanks for registering, ".$name."! You can login using your email&nbsp;<a href=\"login.php\">here</a>.");
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

  
</body>
</html>