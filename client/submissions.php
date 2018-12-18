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
  <title>View Submissions</title>
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/datatables/data-tables.bootstrap4.min.css">
  <link rel="stylesheet" href="assets/socicon/css/styles.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="stylesheet" href="assets/extra/css/extra.css" type="text/css">
  
  
  
</head>
<body>
      <?php
	  include('includes/header.php');
	  ?>

<section class="mbr-section content4 cid-rbRivNiOjv" id="content4-e">

    

    <div class="container">
        <div class="media-container-row">
            <div class="title col-12 col-md-8">
                <h2 class="align-center pb-3 mbr-fonts-style display-2">
                    <br><br><a href="assignment.php">Assignment 1: Hello World Submissions</a></h2>
                <h3 class="mbr-section-subtitle align-center mbr-light mbr-fonts-style display-5">
                    View submitted code and results for Assignment 1</h3>
                
            </div>
        </div>
    </div>
</section>

<section class="progress-bars1 cid-rbRs7N93Kj" id="progress-bars1-l">
    
      

    

    <div class="container">
        

        

        <div class="progress_elements">
            <div class="progress1 pb-5">
                <div class="title-wrap">
                    <div class="progressbar-title mbr-fonts-style display-7">
                        <p>
                            Success Rate</p>
                    </div>
                    <div class="progress_value mbr-fonts-style display-7">
                        <div class="progressbar-number"></div>
                        <span>80%</span>
                    </div>
                </div>
                <progress class="progress progress-primary" max="100" value="80">
                </progress>
            </div>
            
            <div class="progress2 pb-5">
                <div class="title-wrap">
                    <div class="progressbar-title mbr-fonts-style display-7">
                        <p>
                           Average Run Time</p>
                    </div>
                <div class="progress_value mbr-fonts-style display-7">
                    <div class="progressbar-number"></div>
                    <span><br>80 ms</span>
                </div>
                </div>
                <progress class="progress progress-primary" max="100" value="80">
                </progress>
            </div>
            
            <div class="progress3 pb-5">
                <div class="title-wrap">
                    <div class="progressbar-title mbr-fonts-style display-7">
                        <p>
                            Average File Length</p>
                    </div>
                    <div class="progress_value mbr-fonts-style display-7">
                        <div class="progressbar-number"></div>
                        <span><br>90 lines</span>
                    </div>
                </div>
                <progress class="progress progress-primary" max="100" value="90">
                </progress>
            </div>
            
            
        </div>
    </div>
</section>

<section class="section-table cid-rbRsNXCUci" id="table1-m">

  
  
  <div class="container container-table">
      
      
      <div class="table-wrapper">
        <div class="container">
          
        </div>

        <div class="container scroll">
          <table class="table" cellspacing="0">
            <thead>
              <tr class="table-heads ">
                  
                  
                  
                  
              <th class="head-item mbr-fonts-style display-7">
                      Name</th><th class="head-item mbr-fonts-style display-7">
                      NetID</th><th class="head-item mbr-fonts-style display-7">
                      Submission Time</th><th class="head-item mbr-fonts-style display-7">
                      Success</th><th class="head-item mbr-fonts-style display-7">
                      Run Time</th><th class="head-item mbr-fonts-style display-7">
                      File Length</th></tr>
            </thead>

            <tbody>
              
              
              
              
            <tr> 
                
                
                
                
              <td class="body-item mbr-fonts-style display-7">A</td><td class="body-item mbr-fonts-style display-7">aaa000</td><td class="body-item mbr-fonts-style display-7">2018-11-17 23:59:59</td><td class="body-item mbr-fonts-style display-7">Yes</td><td class="body-item mbr-fonts-style display-7">50ms</td><td class="body-item mbr-fonts-style display-7">23 lines</td></tr><tr>
                
                
                
                
              <td class="body-item mbr-fonts-style display-7">B</td><td class="body-item mbr-fonts-style display-7">bbb111</td><td class="body-item mbr-fonts-style display-7">2018-11-17 23:59:59</td><td class="body-item mbr-fonts-style display-7">No</td><td class="body-item mbr-fonts-style display-7">50ms</td><td class="body-item mbr-fonts-style display-7">15 lines</td></tr><tr>
                
                
                
                
              <td class="body-item mbr-fonts-style display-7">C</td><td class="body-item mbr-fonts-style display-7">ccc222</td><td class="body-item mbr-fonts-style display-7">2018-11-17 23:59:59</td><td class="body-item mbr-fonts-style display-7">Yes</td><td class="body-item mbr-fonts-style display-7">50ms</td><td class="body-item mbr-fonts-style display-7">28 lines</td></tr><tr>
                
                
                
                
              <td class="body-item mbr-fonts-style display-7">D</td><td class="body-item mbr-fonts-style display-7">ddd333</td><td class="body-item mbr-fonts-style display-7">2018-11-17 23:59:59</td><td class="body-item mbr-fonts-style display-7">Yes</td><td class="body-item mbr-fonts-style display-7">50ms</td><td class="body-item mbr-fonts-style display-7">24 lines</td></tr><tr>
                
                
                
                
              <td class="body-item mbr-fonts-style display-7">E</td><td class="body-item mbr-fonts-style display-7">eee444</td><td class="body-item mbr-fonts-style display-7">2018-11-17 23:59:59</td><td class="body-item mbr-fonts-style display-7">Yes</td><td class="body-item mbr-fonts-style display-7">50ms</td><td class="body-item mbr-fonts-style display-7">10 lines</td></tr></tbody>
          </table>
        </div>
        <div class="container table-info-container">
          
        </div>
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