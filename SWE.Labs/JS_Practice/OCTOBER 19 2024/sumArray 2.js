function sumArray (arr){
    result = 0
    for (var i = 0; i < arr.length; i++)
        result += arr[i]
    return result
}

console.log(sumArray([1, 2, 3, 4])); // 10
console.log(sumArray([5, 10, 15])); // 30