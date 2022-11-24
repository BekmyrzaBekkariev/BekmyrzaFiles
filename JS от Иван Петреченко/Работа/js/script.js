'use sctrict';

// a = 15;
// console.log(a);
// console.log(1);

// let number = 5;
// const leftBordWidth = 1;

// number = 10;
// console.log(number);

// const obj = {
//     a:50
// };
// obj.a = 5;
// console.log(obj);

// let number = 4;
// console.log(1+1);
// console.log('string' * 9);

// const persone = `Alex`;

// const bool  = true;
// let bean = false;

// console.log(something);

// let num;
// console.log(num);

// let obj = {
//     name: 'Alex',
//     age: 25,
//     isMaried: false
// };
// console.log(obj);
// console.log(obj.name);
// // console.log(obj['age']);

// let arr =['plump.png','orange.jpg', 6, 'apple.bmp', {}, []];
// console.log(arr[0]);

// console.log('Hello!');

// let result = confirm("Are you here?");
// console.log(result);

// const answer = +prompt("Вам есть 18?", "18");
// console.log(answer + 5);
// console.log(typeof(answer));

// const answers = [];

// answers[0] = prompt("Ваше имя: ", "");
// answers[1] = prompt("Ваше фамилия: ", "");
// answers[2] = prompt("Возраст: ","");

// document.write(answers);
// console.log(answers);
// console.log(typeof(answers));

// const category = 'toys';
// console.log(`https/someurl.com/${category}/5`);

// const user = 'Ivan';
// console.log(`Hello ${user}`);

// console.log(4 + +'5');

// let incr = 10,
//     dicr = 10;

// incr++;
// dicr--;

// console.log(incr,dicr);

// console.log(2*4 == 8);

// console.log(5%2);

// const isChecked = true,
//       isCase = true;

// console.log(isChecked && isCase);
// console.log(isChecked || isCase);

// console.log(2 + 2 * 2 !== 8);

//№012 Фильмы

// const numberOfFilms = prompt("Cколько фильмов вы уже просмотрели?");

// const personalMovieDB = {
//     count: numberOfFilms,
//     movies: {
//         nameFilm: Filmestimation
//     },
//     actors: {},
//     genres: [],
//     privat: false
// };
// const nameFilm = prompt("Один из последних просмотренных фильмов?", ""),
//       Filmestimation = prompt("На сколько оцените его?", "");
// console.log(personalMovieDB.movies);

// Решение

// const numberOfFilms = +prompt('Cколько фильмов вы уже просмотрели?','');

// const personalMovieDB = {
//     count: numberOfFilms,
//     movies: {},
//     actors: {},
//     genres: [],
//     privat: false
// };

// const a = prompt('Один из последних просмотренных фильмов?'),
//       b = prompt('На сколько оцените его?');

// personalMovieDB.movies[a] = b;

// console.log(personalMovieDB);

// if (4 == 9){
//     console.log('OK!');
// }else {
//     console.log('Error');
// }

// const num = prompt();

// if (num <= 49) {
//     console.log('Мало');
// } else if (num < 100) {
//     console.log('Много');
// }else if (num === 50){
//     console.log('Мадодец!');
// }else {
//     console.log('Ты Чё');
// }

// const num = 40;

// (num == 42) ? console.log('Ok!') : console.log('Error');

// const num  = 51;

// switch (num) {
//     case 44:
//         console.log('Не верно');
//         break;
//     case 100:
//         console.log('Да чтож такое!');
//         break;
//     case 50:
//         console.log('В точку');
//         break;
//     default:
//         console.log('Ничего страшного');
//         break;
// }

// let num = 50;

// while (num <= 55) {
//     console.log(num);
//     num++;
// }

// do {
//     console.log(num);
//     num++;
// }
// while (num < 57);

// for ( let i = 1; i < 11; i++) {
//     console.log(i);
// }

// for ( let i = 1; i < 11; i++ ) {
//     console.log(num);
//     num++;
// }

// for (let i = 1; i < 10; i++) {
//     if ( i == 6 ){
//         // break;
//         continue;
//     }
//     console.log(i);
// }

// Практика ч2

// const numberOfFilms = prompt('Cколько фильмов вы уже просмотрели?','');

// const personalMovieDB = {
//     count: numberOfFilms,
//     movies: {},
//     actors: {},
//     genres: [],
//     privat: false
// };
// #1 Цыкл
// for (let i=0; i<1; i++){
//     let a = prompt('Один из последних просмотренных фильмов?'),
//         b = prompt('На сколько оцените его?');

//     if (a != null && b != null && a != '' && b != '' && a.length < 50 && b.length < 50){
//         personalMovieDB.movies[a] = b;
//         console.log('Done1');
//     }else {
//         console.log('err0r2');
//         i--;
//     }
// }

// #2 Цыкл
// let i = 0;
// while (i<1){
//     let a = prompt('Один из последних просмотренных фильмов?'),
//         b = prompt('На сколько оцените его?');
//     if (a != null && b != null && a != '' && b != '' && a.length < 50 && b.length < 50) {
//         personalMovieDB.movies[a] = b;
//         console.log('Done1');
//     }else {
//         console.log('err0r2');
//         i--;
//     }
//     i++;
// }

// #3 Цыкл
// let i = 0;
// do {
//     let a = prompt('Один из последних просмотренных фильмов?'),
//         b = prompt('На сколько оцените его?');

//     if (a != null && b != null && a != '' && b != '' && a.length < 50 && b.length < 50) {
//         personalMovieDB.movies[a] = b;
//         console.log('Done1');
//     }else {
//         console.log('err0r2');
//         i--;
//     }
//     i++;
// }
// while (i < 1);

// if (personalMovieDB.count < 10) {
//     console.log('Просмотренно довольно мало фильмов');
// }else if (personalMovieDB.count >= 10 && personalMovieDB.count < 30) {
//     console.log('Вы класический зритель');
// }else if (personalMovieDB.count > 30) {
//     console.log('Вы киноман');
// }else {
//     console.log('Произошла ошибка');
// }

// console.log(personalMovieDB);

// function showFirstMassage() {
//     console.log("Hello World!");
// }
// showFirstMassage();

// let num = 20;

// function showFirstMassage (text) {
//     console.log(text);
//     console.log(num);
// }
// showFirstMassage("Hi every one!");
// console.log(num);

// function calc (a,b) {
//     return (a + b);
// }
// console.log(calc(33,11));
// console.log(calc(5,6));
// console.log(calc(51,63));

// function ret() {
//     let num = 50;
//     //

//     return num;
// }
// const another = ret();
// console.log(another);

// logger2();
// function logger2 () {
//     console.log('Jambi');
// }

// logger();
// const logger = function() {
//     console.log('Jambo');
// };

// logger();

// const calc = (a,b) => {
//     return a + b;
// };

// calc(3,5);

// const str = "tEsT";
// console.log(str.length);
// console.log(str.toUpperCase());
// console.log(str.toLowerCase());

// const frute = "Some frute";
// console.log(frute.indexOf("Some"));
// console.log(frute.indexOf("q"));

// const logg = "Hello world";

// console.log(logg.slice(0,5));

// console.log(logg.substring(0,5));

// console.log(logg.substr(6, 4));

// const num = 12.34546;

// console.log(Math.round(num));

// const test = '15.6px';
// console.log(parseInt(test));
// console.log(parseFloat(test));

// // Практика ч3~~

// let numberOfFilms;

// function start() {
//     numberOfFilms = +prompt('Cколько фильмов вы уже просмотрели?','');

//     while(numberOfFilms == '' || numberOfFilms == null || isNaN(numberOfFilms)){
//         numberOfFilms = +prompt('Cколько фильмов вы уже просмотрели?','');
//     }
// }

// // start();

// const personalMovieDB = {
//     count: numberOfFilms,
//     movies: {},
//     actors: {},
//     genres: [],
//     privat: true
// };

// function remeberMyFilm () {
//     for (let i=0; i<1; i++) {
//         const a = prompt('Один из последних просмотренных фильмов?'),
//               b = prompt('На сколько оцените его?');

//         if (a != null && b != null && a != '' && b != '' && a.length < 50 && b.length < 50){
//                 personalMovieDB.movies[a] = b;
//                 console.log('Done1');
//         }else {
//             console.log('err0r2');
//             i--;
//         }
//     }
// }

// // remeberMyFilm();

// function detectPersonalLevel() {
//     if (personalMovieDB.count < 10) {
//         console.log('Просмотренно довольно мало фильмов');
//     }else if (personalMovieDB.count >= 10 && personalMovieDB.count < 30) {
//         console.log('Вы класический зритель');
//     }else if (personalMovieDB.count > 30) {
//         console.log('Вы киноман');
//     }else {
//         console.log('Произошла ошибка');
//     }
// }

// // detectPersonalLevel();

// function showMyDB (hidden) {
//     if (!hidden) {
//         console.log(personalMovieDB);
//     }
// }
// showMyDB();

// function writeYourGenres() {
//     for (let i = 1; i <= 3; i++) {
//         personalMovieDB.genres[i-1] = prompt(`Ваш любимый жанр под номерам ${i}`);
//     }
// }
// writeYourGenres();

// function first() {
//     setTimeout(function() {
//         console.log(1);
//     }, 1000);
// }

// function second() {
//     console.log(2);
// }

// first();
// second();

// function learnJS(lang, callback) {
//     console.log(`Я учу: ${lang}`);
//     callback();
// }

// function done() { // функция имеющий переменную
//     console.log('Я прошел этот урок!');
// }

// learnJS('JavaScript', function() { // Это анонимная функция
//      console.log('Я прошел этот урок!');
// });

// learnJS('JavaScript', done);

let counter = 0;
const options = {
  name: 'test',
  width: 1024,
  height: 1024,
  colors: {
    border: 'black',
    bg: 'red',
  },
  makeTest: function () {
    console.log('Tesla');
  },
};
// delete options.name;
options.makeTest();

console.log(Object.keys(options).length);

const { border, bg } = options.colors;
console.log(border);

// Перебо обьекта
for (let key in options) {
  if (typeof options[key] === 'object') {
    for (let i in options[key]) {
      console.log(`Свойство ${i} имеет значение ${options[key][i]}`);
    }
  } else {
    console.log(`Свойство ${key} имеет значение ${options[key]}`);
    counter++;
  }
}
console.log(counter);
