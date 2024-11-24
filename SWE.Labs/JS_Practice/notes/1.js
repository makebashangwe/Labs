let person = {
    name: 'Mosh', //properties
    age: 30,
}; //object literal

//dot notation to access , more concise, common

person.name = 'John';

console.log(person.name)

//bracket notation to access property, better for unknown target property
person['name'] = 'Mary';

console.log(person.name);

let selectedColors = []; //array literal
selectedColors = ['red', 'blue']
selectedColors[2] = 1; // length & type dynamic, int inferred and added in index 2

console.log(selectedColors[0]); // access index red

//array properties
console.log(selectedColors.length);


//functions
function greet(name){
    console.log("Hello, " + name);
}

name = 'john'
greet(name);

function square(number){
    return number*number
}
let number = square(2);
console.log(number);

//or console.log(square(2))

//math
var myVar = 11;
myVar -- //number is 10
myVar++ //number is 12
// 
//\' is to have a quote character within a string or u can do single or double quotes usingthis method

var myArray = [[44,42], [22,23]];
console.log(myArray[0][0])

isEnabled = false
let johnAge = 30;
if (johnAge < 100) {
    console.log("yes it is true, he is young!") ;
    isEnabled = true
}
console.log(isEnabled)
/* 
for (var i = 0; i<5; i++){ ----> a variable i = 0, while the i is less than 5, add 1
    our Array.push(i) ---> fills array with  1-4
}
*/
