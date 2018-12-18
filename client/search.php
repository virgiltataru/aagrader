<?php
	include('includes/database.php');
	include('includes/session.php');
	include('includes/functions.php');
	$search = $_GET['q'];
	$class = $_GET['c'];
	if ($search != "") {
		$suggestion = array();
		global $conn;
		if ($class != "") {
			$sth = $conn->query("SELECT * FROM courses WHERE course_id='".$_GET['c']."'");
			$result = $sth->fetch();
			if (is_array($result)) {
				$sth = $conn->query("SELECT id FROM students_courses where course_id = ".$class);
				$curr = array();
				while ($row = $sth->fetch()) {
					array_push($curr, $row);
				}
				$list = array();
				foreach  ($curr as $currs) {
					array_push($list, $currs['id']);
				}
				$exclude = implode(",", $list);
				if ($exclude == "") {
					$exclude = 0;
				}
				$query = "SELECT a.id, a.email, a.name, a.teacher FROM accounts a WHERE a.id NOT IN (".$exclude.")";
			}
		}
		if (!isset($query)) {
			$query = "SELECT a.id, a.email, a.name, a.teacher FROM accounts a";
		}
		$sth = $conn->query($query);
		$students = array();
		while ($row = $sth->fetch()) {
			array_push($students, $row);
		}
		foreach ($students as $student) {
			if ((strpos($student['email'], $search) !== false) && ($student['teacher'] == 0)) {
				array_push($suggestion, "<a href=\"add_to_course.php?cid=".$class."&id=".$student['id']."\">".$student['email']." ".$student['id']."</a>");
			}
		}
	}
	if (count($suggestion) == 0) {
		$output = "no results found";
	}
	else {
		$u_suggestion = array_unique($suggestion);
		$output = implode("<br>", $u_suggestion);
	}
	echo($output);
?>
