function getFullName(person){
return person.firstName + " " + person.lastName; //Concatenate
}

const person = { firstName: "Jane", lastName: "Doe" };
console.log(getFullName(person));