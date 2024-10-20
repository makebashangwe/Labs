function factorial(n){
    result = 1
    for (var i=0; i<n+1; i++)
    {
    result += n * result
    n -= 1
    }
    return result
}

console.log(factorial(5))