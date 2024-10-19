const nums = [1, 2, 3, 4, 5, 6];

function filterEvenNumbers(nums){
    evenNumbers = []
    for (var i=0; i<nums.length; i++){
        if (nums[i] % 2 ==0){
            evenNumbers.push(nums[i])
        }
        else{
            null
        }

    }
    return evenNumbers
}

console.log(filterEvenNumbers(nums));