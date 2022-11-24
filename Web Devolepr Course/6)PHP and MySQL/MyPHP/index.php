<?php
//-------------------------------------
// $name = "John";
// $lastname = "Black";
// echo $name." ".$lastname;
// $x = 23;
// $y = 17;
// $sum = $x + $y;
// echo "<p>$sum</p>";
// $variableName = "lastname";
// echo $$variableName;
//-------------------------------------

// $colors = array("red","orange","blue","green");
// $colors[] = "yellow";
// print_r($colors);
// echo $colors[2];
// echo "<br>";
// echo "<br>";
// $names[0] = "Jane";
// $names[1] = "Jake";
// $names[5] = "Jim";
// $names["name"] = "Jec";
// unset($names[5]);
// echo sizeof($names);
// print_r($names);
// echo "<br>";
// echo "<br>";
// echo $names["name"];
// $yers["Jane"] = 1999;
// $yers["Jane"] = 1989;
// $yers["Jane"] = 2009;
// echo "<br>";
// print_r($yers);
// --------------------------------

// $userName = "joe";
// $userAge = 15;
// $isUserLogin = true;
// // ||- или; &&-и;
// if ($isUserLogin || $userAge >= 18) {
// 	echo "Hello".$userName;
// }else {
// 	echo "You have to login and you have to be older then 18";
// }
//-----------------------------------------------------

// $colors = array("red","orange","yellow", "green", "blue" , "indigo", "violet");

// foreach ($colors as $key => $value) {
// 	$colors[$key] = $value." color";
// 	echo $key." ".$value;
// }

// for ($i=0; $i < sizeof($colors); $i++) {
// 	echo $colors[$i]."<br>";
// }

//---------------------------------------------------

// $i = 1;

// while ($i <= 10) {

// 	$y = $i * 7;

// 	echo $y."<br>";

// 	$i++;
// }

// $colors = array("red","orange","yellow", "green", "blue" , "indigo", "violet");

// $i = 0;

// while ($i <= sizeof($colors)) {
	
// 	echo $colors[$i]."<br>";

// 	$i++;
// }
// =GET---------------

// print_r($_GET);
// echo "hello".$_GET["userName"];

// --------------------

// Четное и нечетное

// if (isset($_GET["number"])) {
// 	$value = $_GET["number"];

// 	if(floor($value) == $value && is_numeric($value)){

// 	if ($value%2) {
// 	echo $value." is odd";		
// 	}else {
// 	echo $value." is even";
// 	}
// 	}else {
// 	echo "Input the whole number";
// 	}
// }
//---------------------------------


// $login = array('yora' =>'1111' , );
// if ($login[0]=[1]) {
// 	echo "1";
// }else{
// 	echo "2";
// }
//-----------------------------------
//Запрашиватель пороля ИИУ!

	// $loginPasswordArray = array(
	
	// 	"coolDaddy" => "11111",
	// 	"Jane" => "22222",
	// 	"admin" => "admin",
	// 	"Kay" => "bekmyrzabekmyrza05"
	// );

	// $isLoginPasswordCorrect = false;

	// if (isset($_POST["login"]) && isset($_POST["password"])){
	// 	foreach ($loginPasswordArray as $key => $value) {
	// 		if ($key == $_POST["login"] && $value == $_POST["password"]) {
	// 			$isLoginPasswordCorrect = true;
	// 		}
	// 	}

	// 	if ($isLoginPasswordCorrect) {
	// 		echo "Hello ".$_POST["login"]."!";
	// 	} else {
	// 		echo "Please input correct login and password";
	// 	}
	// }
//--------------------------------
	// include("otherFile.php");

	// echo file_get_contents("https://google.com/");
// --------------------------------------------------------
?>

<!-- <p>Input your login and password</p>

<form method="post">

	<p><input type="text" name="login"></p>
	<p><input type="password" name="password"></p>
	<p><input type="submit" name=""></p>

</form> -->