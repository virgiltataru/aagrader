<?php
	session_start();
	if (isset($_SESSION["most_recent"])) {
		if (time() - $_SESSION["most_recent"] > 1800) {
			session_destroy();
			session_unset();
			header('LOCATION:./timeout.php');
			die();
		}
		else if (time() - $_SESSION["most_recent"] > 300) {
			session_regenerate_id();
		}
		echo($_SESSION["most_recent"] - time());
		$_SESSION["most_recent"] = time();
	}
?>