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
	$sth = $conn->prepare("DELETE FROM students_courses WHERE id = ".$id." AND course_id = ".$class)->execute();
	unset($_SESSION['continue']);
	header('LOCATION:course.php?id='.$class.'&r=1');
?>