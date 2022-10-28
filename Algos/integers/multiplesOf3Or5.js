// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 

// Additionally, if the number is negative, return 0 (for languages that do have them).
// Note: If the number is a multiple of both 3 and 5, only count it once.

const solution = number => {
    let sum = 0;
    let num = number - 1;
    if (number < 0) return 0;
    // just see if the % 3 || % 5 === 0 then sum them all up
    // BUT you need to loop through the numbers first to catch all the multiples
    for (let i = num; i > 0; i--){
        if (i % 3 === 0 || i % 5 === 0){
            sum += i;
        }
    }
    return sum;
}

console.log(solution(10));
console.log(solution(23));