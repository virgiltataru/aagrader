<?php
	include("database.php");
	function getAccountCourses($id) {
		global $conn;
		$sth = $conn->query("SELECT c.course_id, c.name, c.location, c.time, c.active FROM accounts a, courses c, students_courses s WHERE a.id = s.id AND c.course_id = s.course_id AND a.id = ".$id);
		$result = array();
		while ($row = $sth->fetch()) {
			array_push($result, $row);
		}
		return $result;
	}
	function getStudentsEnrolled($id) {
		global $conn;
		$sth = $conn->query("SELECT a.id, a.email, a.name FROM accounts a, courses c, students_courses s WHERE a.id = s.id AND c.course_id = s.course_id AND c.course_id = ".$id);
		$result = array();
		while ($row = $sth->fetch()) {
			array_push($result, $row);
		}
		return $result;
	}
	function getCourseTeachers($id) {
		global $conn;
		$sth = $conn->query("SELECT a.id, a.email, a.name FROM accounts a, courses c, teachers_courses t WHERE a.id = t.id AND c.course_id = t.course_id AND c.course_id = ".$id);
		$result = array();
		while ($row = $sth->fetch()) {
			array_push($result, $row);
		}
		return $result;
	}
?>