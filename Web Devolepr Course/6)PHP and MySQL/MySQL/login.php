<?php 

# Выыод данных 
	// if (isset($_POST['submit'])) {
	// 	$email = $_POST['email'];
	// 	$password = $_POST['password'];

	// 	// echo $email;
	// 	// echo $password;

	// 	$connection = mysqli_connect('localhost', 'root', '', 'my-database');

	// 	$query = 'SELECT * FROM user;';

	// 	if ($connection) {
	// 		$query_result = mysqli_query($connection, $query);
	// 		if ($query_result) {
	// 			$data_array = mysqli_fetch_array($query_result);
	// 			echo "Hello"." ".$data_array['user_name']."! Your email is ".$data_array['email']." "."and your password is " .$data_array['password'];
	// 		}
	// 	} else {
	// 		die('Conection failed');
	// 	}
	// } 

# Вставка данных

	if (isset($_POST['submit'])) {
		$email = $_POST['email'];
		$password = $_POST['password'];
		$username = $_POST['username'];

		// echo $email;
		// echo $password;

		$connection = mysqli_connect('localhost', 'root', '', 'my-database');


		if ($connection) {
			echo "Database is connected";
		} else {
			die('Conection failed');
		}


		$query = "INSERT INTO user (user_name, email, password) VALUES ('$username', '$email','password');";

		$query_result = mysqli_query($connection, $query);

		if (!$query_result){
			die("Query failed ".mysqli_error());
		}
	}


?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
	<title>Document</title>
</head>
<body>
	
	<form action="login.php" method="post">
		<div class="mb-3">
	    <label for="exampleInputUsername1" class="form-label">Username</label>
	    <input type="form-text" class="form-control" name="username" id="exampleInputUsername1" aria-describedby="emailHelp" placeholder="Enter your name">
	    
	  </div>
	  <div class="mb-3">
	    <label for="exampleInputEmail1" class="form-label">Email address</label>
	    <input type="email" class="form-control" name="email" id="exampleInputEmail1" aria-describedby="emailHelp">
	    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
	  </div>
	  <div class="mb-3">
	    <label for="exampleInputPassword1" class="form-label">Password</label>
	    <input type="password" class="form-control" name="password" id="exampleInputPassword1">
	  </div>
	  <div class="mb-3 form-check">
	    <input type="checkbox" class="form-check-input" id="exampleCheck1">
	    <label class="form-check-label" for="exampleCheck1">Check me out</label>
	  </div>
	  <button type="submit" class="btn btn-primary" name="submit">Submit</button>
	</form>

</body>
</html>