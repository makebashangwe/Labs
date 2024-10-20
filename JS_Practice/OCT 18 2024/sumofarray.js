function sumArray(nums){
    result = 0;
    for (var i = 0; i<nums.length; i++){
        result += nums[i];
    };
    return result;
}

const numbers = [1, 2, 3, 4];
console.log(sumArray(numbers));