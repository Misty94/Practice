// Input: a positve integer
// Output: the param's multiplicative persistence (the number of times you must multiply the digits in the param until you reach a single digit)
/*
Examples: 
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
 */

const persistence = num => {
    let product = 1;
    let count = 0;
    if (num.length === 1) return 0;
    for (let i = 0; i < product.length; i++){
        
    }
}