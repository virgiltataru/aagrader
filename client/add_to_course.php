<?php
	include('includes/database.php');
	include('includes/session.php');
	include('includes/functions.php');
	if (!isset($_SESSION['continue'])) {
		header('LOCATION:index.php');
		die();
	}
	$id = $_GET['id'];
	$class = $_GET['cid'];
	if (($id == "") || ($class == "")) {
		header('LOCATION:index.php');
		die();
		}
	global $conn;
	$sth = $conn->prepare("INSERT INTO students_courses (id, course_id) VALUES (?, ?)")->execute([(int)$id, (int)$class]);
	unset($_SESSION['continue']);
	header('LOCATION:course.php?id='.$class.'&s=1');
?>