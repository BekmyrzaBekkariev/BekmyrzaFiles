// jQuery('document').ready(function(){
	// jQuery('body').append('<a href="">Перейти в...</a>');
	// jQuery('hr').remove();

	// var p_clon;

	// p_clon = jQuery('p').clone();

	// jQuery('body').append(p_clon);

	// var p1,p2;

	// p1 = 25;
	// p2 = p1;
	// alert(p1 + p2);

	// alert(Math.sqrt(5*5))

// 	var katet1,katet2;
// 	katet1 = 10;
// 	katet2 = 20;

// 	var katet1_sq, katet2_sq;
// 	katet1_sq = katet1 * katet1;
// 	katet2_sq = katet2 * katet2;

// 	var kvadr_gepa;
// 	kvadr_gepa = Math.sqtr(katet1_sq + katet2_sq);

// 	var kvadr_dlin;
// 	kvadr_dlin = Math.sqtr(kvadr_gepa);

// 	alert(kvadr_dlin);


	// jQuery('button').on('click',function(){
	// 	var value1, value2, value3;
	// 	value1=jQuery('#val1').val();
	// 	value2=jQuery('#val2').val();
	// 	value1=parseInt(value1);
	// 	value2=parseInt(value2);
	// 	value3=value1+value2;
	// 	alert(value3);
		

	// });
	// jQuery('input').on('keyup',function(){
	// 	var value1, value2, value3;
	// 	value1=jQuery('#val1').val();
	// 	value2=jQuery('#val2').val();
	// 	value1=parseInt(value1);
	// 	value2=parseInt(value2);
	// 	value3=value1*value2;
	// 	jQuery('#rezultat').html(value3);
	// });


	//var test1;
	//test1 = prompt('Ведите ваше имя:','Алексей');
	//jQuery('#rezultat').html(test1);
	// test1=confirm('EE&')


	// var a1 = 555;
	// if (a1==555){
	// 	alert('Good');
	// }else{
	// 	alert('False');
	// }

// 	var pogoda = 'дождь'
// 	var time = 'ночь'

// 	if ((pogoda == 'солнечно' || pogoda == 'облачно')&& time == 'день'){
// 		alert('Можно ехать на пикник! Ураа!');
// 	}else if (pogoda == 'дождь' && time == 'день'){
// 		alert('еать можно , но нужно взять зонты!');
// 	}else{
// 		if(time == 'день'){
// 			alert('На пикник ехать нельзя плохая погода. Сейчас ведь'+pogoda+'.\nКакой-там блин пикник...');
// 		}else{

// 			var message = 'Какой-там пикник Сейчас же дождь!!!';
// 			if(pogoda == 'дождь'){
// 				message = message + '\nКтому же льет дождь ты совсем чтоли дурак';
// 			}
// 			alert(message);
// 		}
// 	}
// });



// var roSt = prompt('Ведите ваш рост в метрах');
// var aGe = prompt('Ведите ваш возраст')
// var ves = prompt('ведите ваш вес');

// var reshenie = ves / (roSt * roSt);
// var groupNumber;

// if(aGe >= 18 && aGe <= 25){
// 	groupNumber = 1;
// }else if(aGe >25 && aGe <= 46){
// 	groupNumber = 2;
// }else{
// 	groupNumber =3;
// }

// if (groupNumber === 1 && reshenie < 17.5){
// 	alert("Недостаточен, опасно для здоровья");
// }else if (groupNumber === 1 && reshenie >= 17.5 && reshenie < 19.5){
// 	alert("Слегка снижен, неопасно для здоровья")
// }else if (groupNumber === 1 && reshenie >= 19.5 && reshenie < 23){
// 	alert("Ваш вес нормальный");
// }else if (groupNumber === 1 && reshenie >= 23 && reshenie < 27.5){
// 	alert("Ваш вес Излишний");
// }else if (groupNumber === 1 && reshenie >= 27.5 && reshenie < 30){
// 	alert("Ожирение 1 степени");
// }else if (groupNumber === 1 && reshenie >= 30 && reshenie < 35){
// 	alert("Ожирение 2 степени");
// }else if (groupNumber === 1 && reshenie >= 35 && reshenie < 40){
// 	alert("Ожирение 3 степени");
// }else if (groupNumber === 1 && reshenie >= 40){
// 	alert("Ожирение 4 степени");

// } else if (groupNumber === 2 && reshenie < 18){
// 	alert("Недостаточен, опасно для здоровья");
// }else if (groupNumber === 2 && reshenie >= 18 && reshenie < 20){
// 	alert("Слегка снижен, неопасно для здоровья")
// }else if (groupNumber === 2 && reshenie >= 20 && reshenie < 26){
// 	alert("Ваш вес нормальный");
// }else if (groupNumber === 2 && reshenie >= 26 && reshenie < 28){
// 	alert("Ваш вес Излишний");
// }else if (groupNumber === 2 && reshenie >= 28 && reshenie < 31){
// 	alert("Ожирение 1 степени");
// }else if (groupNumber === 2 && reshenie >= 31 && reshenie < 36){
// 	alert("Ожирение 2 степени");
// }else if (groupNumber === 2 && reshenie >= 36 && reshenie < 41){
// 	alert("Ожирение 3 степени");
// }else if (groupNumber === 2 && reshenie >= 41){
// 	alert("Ожирение 4 степени");
// }else if(groupNumber === 3){
// 	alert("нет данных для вашего возраста");
// }





// var firstName, lastName, fulname, age;
// firstName = "vasya";
// console.log(firstName);
// firstName = "Peta";
// console.log(firstName);
// lastName = "Ivanov";
// console.log(lastName);
// fulname = firstName +" " + lastName;
// console.log(fulname);
// age = 15;
// console.log(age);
// var pleyer = "fd"
// pleyer = null;
// console.log(pleyer);
// var firstName = "vasya";
// firstName = prompt("what is your name?");
// console.log(firstName);

// var firstName, lastName, age;
// firstName = prompt("what is your name?");
// lastName = prompt("what is your lastName?");
// age = prompt("what is your age?")
// console.log("Пользователь:" + firstName + " " + lastName);
// console.log("Возраст:"+ " " + age);

// var numberOfDollars = prompt("Веите сколько доларов нужно перевсти");
// alert("Вы получите" + " " +numberOfDollars * 84.78 + "сомов" );

// var x = 5;
// var y = "5";
// var isXMore = x === y;

// console.log(isXMore);

// var y = 10;
// x = ++y;
// console.log(x,y);

// var rost = prompt("Ведите ваш рост в метрах");
// var kg = prompt("Ведите ваш вес в килограммах");
// var reshenie = kg/(rost*rost);
// var itog = reshenie > 28;
// alert("У вас лишний вес:"+ " " + itog); 

// var x = prompt("Веди пороль:");
// if (x == 12345, x == 123){
// 	alert("Welkom");
// }else{
// 	alert("GO ne nash")
// }

// var rost = prompt("Ведите ваш рост в метрах");
// var kg = prompt("Ведите ваш вес в килограммах");
// var reshenie = kg/(rost*rost);
// if(reshenie >= 28){
// 	alert("Ты жирный");
// }else{
// 	alert("Воу норм так держать!");
// }

// var userName = prompt("whar is your name");
// var userAge = prompt("whar is your age");

// if (userAge>=18){
// 	alert(userName +" "+ "привет взрослый");
// }else{
// 	alert("привет юнуша");
// }



// var userName = "Jack";
// var userWeight = 87;

// if(userWeight > 90 ){
// 	console.log(userName + "2")
// }else{
// 	console.log(userName + "3")
// }

// userName > 90 ? console.log(userName + "2") : console.log(userName + "3");

// var x = 10;
// var y = 11;
// y >= 11 ? console.log(2) : console.log(4);



// var section ="javascript";

// switch (section) {
// 	case "html" :
// 		console.log("вы изучаете раздел 'HTML' ");
// 		break;
// 	case "css" :
// 		console.log("вы изучаете раздел 'CSS' ");
// 		break;
// 	case "javascript" :
// 		console.log("вы изучаете раздел 'JavaScript' "); 
// 		break;
// 	default :
// 		console.log("вы изучаете другой язык");
// }


// var userName = prompt("Веди что надо");

// switch ( userName){
// 	case "12345" :
// 		console.log("Вау как");
// 		break;
// 	case "jack" :
// 		console.log("норм");
// 		break;
// 	default :
// 		console.log("Мдаа не фортануло")
// }


// var aGe = 10;
// var groupNumber;

// if(aGe >= 18 && aGe <= 25){
// 	groupNumber = 1;
// }else if(aGe >25 && aGe <= 46){
// 	groupNumber = 2;
// }else{
// 	groupNumber =3;
// }

// console.log(groupNumber);

// switch(true) {
// 	case aGe >= 18 && aGe <= 25 :
// 		groupNumber = 1;
// 		break;
// 	case aGe >25 && aGe <= 46 :
// 		groupNumber = 2;
// 		break;
// 	default :
// 	groupNumber =3;
// }
  
// console.log(groupNumber);



// var name = prompt("Ведите логин:");
// var password = prompt("Ведите ваш пороль:");
// switch (name , password){
// 	case "Вася":
// 	case "1111":
// 		alert("Добро пожаловат Вася");
// 		break;
// 	case "Ваня":
// 	case "2222":
// 		alert("Добро пожаловат Ваня");
// 		break;
// 	case  "Admin":
// 	case "Admin":
// 		alert("Добро пожаловат Admin Вы можете редактировать сайт");
// 		break;
// 	default:
// 		alert("Ваш логин или пороль не правильный");
// }


//****************РЕШЕНИЕ ЗАДАЧИ PASSWORD*****************************************
// var userName = prompt("Ведите логин:");
// var password = prompt("Ведите ваш пороль:");

// switch (true){
// 	case userName === "Вася" && password === "1111":
// 		alert("Добро пожаловат Вася");
// 		break;
// 	case userName === "Ваня" && password === "2222":
// 		alert("Добро пожаловат Ваня");
// 		break;
// 	case userName === "Лена" && password === "3333":
// 		alert("Добро пожаловат Лена");
// 		break;
// 	case userName === "Джек" && password === "4444":
// 		alert("Добро пожаловат Джек");
// 		break;
// 	case userName === "Админ" && password === "1111":
// 		alert("Добро пожаловат Админ");
// 		break;
// 	default:
// 		alert("Ваш логин или пороль не правильный");
// }


// var x = 1;

// while(x <= 10 ){
// 	console.log(x);
// 	++x;
// }

// var t = 1;

// while(t<5){
// 	console.log(t);
// 	t++;
// }

// var helloString = "Hello JavaScript!"
// var count = 0;

// while(count < helloString.length){
// 	console.log(helloString[count]);
// 	count++;
// }


// var count = 1
// while (  count<5){
// 	console.log(count);
// 	count++;
// }

// for (count = 1; count<=10; count++){
// 	console.log(count);
// }


// for (x = 1; x<= 10; x++){
// 	console.log(x);
// }


// for (y = 1; y <=50; y++){
// 	console.log(y);
// }

// var helloString = "Hello For Loop!";
// for (i = 0; i<helloString.length; i++){Ы
// 	console.log(helloString[i]);
// }

// var rec = "hello of student rechion for is";

// for (i=0; i<rec.length; i++){
// 	console.log(rec[i]);
// }

// var riv = 10;
// for (i=0; i<10; i+2){
// 	console.log(i);
// }

// for (i=0; i<10; i++){
// 	console.log(i);
// }


// Функция*
// function hello(){
// 	console.log("Hello!");
// }
// hello();


// function world(){
// 	console.log("23");
// }
// world();



// function rek(){
// 	console.log("let Gta");
// }
// rek();

// Функция с параметрами 29*

// Квадрат 
// function sqart(number){
// 	console.log(number * number);
// }

// sqart(2);

// function area(width, height){
// 	console.log(width * height);
// }

// area(3,4)


// function complexHello(helloText, name, age){
// 	console.log(helloText + "my name is"+ name + "Im"+ age + "years old");
// }

// complexHello("Hey" ,"John" ,43);
// complexHello("He" ,"Jnive" ,10);
// complexHello("Hi" ,"mikl" ,29);
// complexHello("Hello" ,"rita" ,34);

// 30

// function sq (number){
// 	return number * number;
// }

// var z = sq(2);
// console.log(z);

// function isSqareBig(side) {
// 	var squareArea = sq(side);
// 	if (squareArea > 100) {
// 		return true;
// 	}else{
// 		return false:
// 	}
// }

// console.log(isSqareBig(10));

// function animalVoise(animal, animalName){
// 	switch(animal){
// 		case "dog":
// 			return animalName + " barks ";
// 		case "cat":
// 			return animalName + " meows";
// 		case "pig":
// 			return animalName +  " pig";
// 			default:
// 				return animalName + "makes some";
// 	}
// }

// console.log(animalVoise("cat", "Richard"));


//что то так получилось он не получилось с фун
// var x = "0";
// if (x / 2){
// 	console.log(true);
// }else{
// 	console.log(false);
// }

//#Чётное не четное

// function isNumberOdd(number){
// 	if ( number % 2 === 0 ){
// 		return false;
// 	}else{
// 		return true;
// 	}
// }

// var x = isNumberOdd(11);
// console.log(x);
// console.log(isNumberOdd(0));

// function isNumberOdd(number){
// 	return number % 2 === 0 ;
// }

// var x = isNumberOdd(21);
// console.log(x);
// console.log(isNumberOdd(10));


// //ФАКТОРИАЛ ЧИСЛА УРААААААААААААААААААААА
// function factorial(NaturalNumber){
// 	if (NaturalNumber < 0){
// 		return 0;
// 	}
// 	var result = 1;
// 	for (i = 1; i <= NaturalNumber; i++){
// 		result = result * i;
// 	}
// 	return result;
// }
// console.log(factorial(5));//120


//прыгатель ураааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа

// function changeSpaceToUnderscore(text) {
// 	var resultText = text.replace(/ /g,"_");
// 	return resultText;
// }

// console.log(changeSpaceToUnderscore("я ты он она мы вы все"));


// function someFunction() {
// 	for (var i = 0 ; i < 10; i++) {
// 		console.log(i);
// 	}
// }
// someFunction();
// console.log(i);

// color1 = "red";
// color2 = "orange";
// color3 = "yellow";
// color4 = "green";
// color5 = "blue";
// color6 = "indigo";
// color7 = "violet";

// var reinbowColors = ["red","orange","yellow","green","blue",
// "indigo","violet"];

// console.log(reinbowColors[0]);

// var emtyArray = [];
// var emtyArrayNew = new Array();

// var number = [1,2,3,4,5,6,7,8];
// console.log(number);

// var anyItems = [1,"some text" , null , true];
// console.log(anyItems);


// var names = ["John", "Jane", "Jack", "Jim"];
// console.log(names);
// names[4] = "Jeen";
// var x = names.push("Jeen");
// x = names.push("Ivan");
// console.log(names);
// console.log(x)

// var y = names.pop();
// console.log(names);
// console.log(y);

// x = names.unshift("Uvi");
// console.log(names);
// console.log(x);

// y = names.shift();
// console.log(names);
// console.log(y);

// var z = names.indexOf("Jack");
// console.log(z);

// var toyota = ["Camry", 2010, "sedan", "black" , true];

// var isSedan = toyota.indexOf("sedan") === -1 ?
// console.log("type is not sedan.") :
// console.log("type is sedan");

// var cars = ["Honda", "KIA", "Shumkar", "Mersedes", "Opel", "Toyota"];
// var germanCars = cars.slice(3,5);
// console.log(germanCars);
// console.log(cars);

//--------Oбькты 43---------------------------------------------------------------------------------------------------------------------
// var toyota = ["Camry", 2010, "sedan", "black" , true];

// var carToyota = {
// 	model:"Camry" , 
// 	year: 2010 , 
// 	carBody: "sedan" , 
// 	color: "black" , 
// 	hasAirbag: true
// };
// console.log(carToyota["color"]);
// console.log(carToyota.year);

// carToyota.color = "red";
// console.log(carToyota.color);

// var ty = prompt("");
// var juk ={
// 	model:"j1", 
// 	color: "yellow" , 
// 	hasAirbag: false , 
// 	carBody: "RU"
// }; 
// console.log(juk[ty]);

// var carMazda = {};
// carMazda.year = 2018;
// carMazda.model = "crosover";
// carMazda.carBody = "CX7";
// carMazda.color = "blue";
// carMazda.hasAirbag = false;
// carMazda.dorNumber = 4;

// console.log(carMazda);

// var carOpel = new Object();
// carOpel.model = "hatchback";
// carOpel.year = 2018;
// carOpel.carBody = "CX7";
// carOpel.color = "blue";
// carOpel.hasAirbag = false;
// carOpel.dorNumber = 4;

// console.log(carOpel);

// var number = [[1,2,3],[3,4,5],[6,7,8]];
// console.log(number[0][1]);

// var carToyota = {
// 	model:"Camry" , 
// 	year: 2010 , 
// 	carBody: "sedan" , 
// 	color: "black" , 
// 	hasAirbag: true, 
// 	pets: ["car","bike","moto"]
// };

// console.log(carToyota.pets[0]);

// var sellers = [

// 	{
// 		firstName: "Peter", 
// 		lastName: "Foodman",
// 		regDate: "02.11.2019",
// 		hasDiscount: true,
// 		age: 46,
// 		cars: [{
// 			carProdyser:"fiat",
// 			carModel:"punto"
// 		},
// 		{
// 			carProdyser:"meRsedes",
// 			carModel:"mERS09"
// 		},
// 		{
// 			carProdyser:"bMW",
// 			carModel:"m7"
// 		}]
// 	},
// 	{
// 		firstName: "Ralf", 
// 		lastName: "Man",
// 		regDate: "32.01.2019",
// 		hasDiscount: false,
// 		age: 47
// 	}
// ]

// console.log(sellers[0].cars[1].carModel);


//-----------------------Cars DataBase РЕШЕНИЕ

// var cars = [
// 	{
// 		carProdyser:"mazda",
// 		carModel:"6",
// 		color: "red",
// 		isSelled: false
// 	},
// 	{
// 		carProdyser:"mersedes",
// 		carModel:"c300",
// 		color: "grey",
// 		isSelled: true
// 	},
// 	{
// 		carProdyser:"opel",
// 		carModel:"astra",
// 		color: "green",
// 		isSelled: true
// 	},
// 	{
// 		carProdyser:"fiat",
// 		carModel:"dodlo",
// 		color: "white",
// 		isSelled: false
// 	}
// ]


// for (var  i = 0; i < cars.length;i++) {
// 	if (cars[i].isSelled === false) {
// 		console.log(cars[i]);
// 	}
// }


// cars.forEach(function(car){
// 	if (car.isSelled === false) {
// 		console.log(car);
// 	}
// })

// console.log(cars);

// var carSeller1 = {
// 	firstName: "Jack",
// 	lastName: "white",
// 	regYear: 2017, 
// 	hasDiscount: true,
// 	discountCalarion: function(year){
// 		var discont;
// 		var numberOfyear = 2021 - year;
// 		if( numberOfyear <= 2){
// 			discont = 0;
// 		}else if(( numberOfyear > 2) && (numberOfyear <= 5)){
// 			discont = 20;
// 		}else if( numberOfyear > 5) {
// 			discont = 30;
// 		}
// 		return discont;
// 	}
// }

// console.log(carSeller1.discountCalarion(2019));


//#2 способ 

// var carSeller1 = {
// 	firstName: "Jack",
// 	lastName: "white",
// 	regYear: 2017, 
// 	hasDiscount: true,
// 	discountCalarion: function(){
// 		var discont;
// 		var numberOfyear = 2021 - this.regYear;
// 		if( numberOfyear <= 2){
// 			discont = 0;
// 		}else if(( numberOfyear > 2) && (numberOfyear <= 5)){
// 			discont = 20;
// 		}else if( numberOfyear > 5) {
// 			discont = 30;
// 		}
// 		return discont;
// 	}
// }

// console.log(carSeller1.discountCalarion());


//# 3 способ 

// var carSeller1 = {
// 	firstName: "Jack",
// 	lastName: "white",
// 	regYear: 2016, 
// 	hasDiscount: true,
// 	discount : 0,
// 	discountCalarion: function(){
// 		var discount;
// 		var numberOfyear = 2021 - this.regYear;
// 		if( numberOfyear <= 2){
// 			discount = 0;
// 		}else if(( numberOfyear > 2) && (numberOfyear <= 5)){
// 			discount = 20;
// 		}else if( numberOfyear > 5) {
// 			discount = 30;
// 		}
// 		return discount;
// 	}
// }

// var discount = carSeller1.discountCalarion();
// carSeller1.discount = discount;
// console.log(discount);


//# 4 способ 

// var carSeller1 = {
// 	firstName: "Jack",
// 	lastName: "white",
// 	regYear: 2016, 
// 	hasDiscount: true,
// 	discount : 0,
// 	discountCalarion: function(){
// 		var discount;
// 		var numberOfyear = 2021 - this.regYear;
// 		if( numberOfyear <= 2){
// 			discount = 0;
// 		}else if(( numberOfyear > 2) && (numberOfyear <= 5)){
// 			discount = 20;
// 		}else if( numberOfyear > 5) {
// 			discount = 30;
// 		}
// 		return discount;
// 	}
// }

// carSeller1.discount = carSeller1.discountCalarion();
// console.log(carSeller1);


//# 5 способ 

// var carSeller1 = {
// 	firstName: "Jack",
// 	lastName: "white",
// 	regYear: 2013, 
// 	hasDiscount: true,
// 	discount : 0,
// 	calculateDiscount: function(){
// 		var discount;
// 		var numberOfyear = 2021 - this.regYear;
// 		if( numberOfyear <= 2){
// 			discount = 0;
// 		}else if(( numberOfyear > 2) && (numberOfyear <= 5)){
// 			discount = 20;
// 		}else if( numberOfyear > 5) {
// 			discount = 30;
// 		}
// 		this.discount = discount;
// 	}
// }

// carSeller1.calculateDiscount();
// console.log(carSeller1);