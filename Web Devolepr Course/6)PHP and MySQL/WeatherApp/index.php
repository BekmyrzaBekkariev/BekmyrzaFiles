<?php 

	error_reporting(E_ERROR | E_PARSE);
	
	$weather = "";

	$error = "";

	if (isset($_GET['city'])) {
		$urlContent = file_get_contents('http://api.openweathermap.org/data/2.5/weather?q='.$_GET['city'].'&units=metric&appid=65e7d294c9173803b68c2148b1f8b0db');

		$forcastArray = json_decode($urlContent, true);


		if ($forcastArray['cod'] == 200 ) {

			$weather = 'The weather in '.$_GET['city'].' is '.$forcastArray['weather'][0]['description'];

			$weather = $weather.'. The temperature is '.$forcastArray['main']['temp'].'&#8451;'.'. The speed of wind is '.$forcastArray['wind']['speed'].' m/sec';
		}else {
			$error = "The city name is incorrect, please try another name";
		}

		}

		


?>


<!doctype html>
<html lang="ru">
  <head>
    <!-- Обязательные метатеги -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="styles/style.css">

    <title>Weather App</title>
  </head>
  <body>


  	<div class="container" id="mainDiv">
  		<h1>Wearher In The City</h1>

	<form>
	  <div class="form-group">
	    <label for="city">Input a city name </label>
	    <input class="form-control" id="city"  name="city" aria-describedby="Forcast city" placeholder="Enter city name">
	  </div>

	  	<button type="submit" class="btn btn-primary">Submit</button>
		</form>
  	</div>

  	<div id="forecastDiv">
  		
  			<?php 

  			if ($weather) {
  				echo '<div class="alert alert-primary" role="alert">'.$weather.'</div>';
  			} else if ($error) {
  				echo '<div class="alert alert-danger" role="alert">'.$error.'</div>';
  			}
  				



  			?>
 	 		
		
  	</div>

    






    <!-- Необязательный JavaScript; выберите один из двух! -->
    <!-- Вариант 1: пакет Bootstrap с Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>
    <!-- Вариант 2: отдельные JS для Popper и Bootstrap -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.min.js" integrity="sha384-Atwg2Pkwv9vp0ygtn1JAojH0nYbwNJLPhwyoVbhoPwBhjQPR5VtM2+xf0Uwh9KtT" crossorigin="anonymous"></script>
    -->
  </body>
</html>