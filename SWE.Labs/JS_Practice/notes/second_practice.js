

const obj1 = { name: "Alice", age: 25 };
const obj2 = { age: 30, city: "New York" };

function mergeObjects(obj1,obj2){
    return {...obj1, ...obj2} //spreads the properties of obj1 and 2 into a new object abnd will override conflicting keys
}
console.log(mergeObjects(obj1, obj2))
