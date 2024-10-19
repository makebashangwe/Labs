const nums = [1,2,3,3,4,4,5,6,7,7,9]

function removeDuplicates(nums){
    //return[new Set(nums)] new Set(arr) creates a set from the array arr, automatically removing duplicates.
    //... spread operator spereads the values back into an array
    return[...new Set(nums)]
}

console.log(removeDuplicates(nums))