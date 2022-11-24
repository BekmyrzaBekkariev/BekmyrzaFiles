"use sctrict";

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


// alert('Hello!');

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

const numberOfFilms = +prompt('Cколько фильмов вы уже просмотрели?','');

const personalMovieDB = {
    count: numberOfFilms,
    movies: {},
    actors: {},
    genres: [],
    privat: false
};

const a = prompt('Один из последних просмотренных фильмов?'),
      b = prompt('На сколько оцените его?');

personalMovieDB.movies[a] = b;

console.log(personalMovieDB);