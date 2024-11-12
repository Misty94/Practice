// Write a function that finds the sum of all its arguments.

function sumOfAll(...args) {
    return args.reduce((sum, num) => sum + num, 0);
}

console.log(sumOfAll(1, 2, 3)) // 6
console.log(sumOfAll(8, 2)) // 10
console.log(sumOfAll(1, 2, 3, 4, 5)) // 15
console.log(sumOfAll(10, 65, 9)) // 84


// ... (spread operator) collects all the arguments passed to the function into an array
// reduce() iterates over an array & accumlates a single value based on a provided function
// it takes 2 arguments ~ the value that is being accumulated (total) & the current element being processed
// optional parameters is the index of the current element & the array being processed.



// ******************************************************************


// Can't Make It Work This Way

// const totalSum = () => {
//     let sum = 0;
//     for (let i = 0; i < arguments.length; i++){
//         sum += arguments[i];
//     }
//     return sum;
// }

// console.log(totalSum(4, 4, 4, 4)) // 16
// console.log(totalSum(5, 9, 3)) // 17