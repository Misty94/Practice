// Input: a positve integer
// Output: the param's multiplicative persistence (the number of times you must multiply the digits in the param until you reach a single digit)

/*
Examples: 
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
 */

const persistence = num => {
    let sNum = num.toString();
    let count = 0;
    let product = 1;
    if (num < 10) return 0;
    while (sNum.length > 1){
        for (let i = 0; i < sNum.length; i++){
            product *= sNum[i];
        }
        count++;
        sNum = product.toString();
        product = 1;
    }
    return count;
}

console.log(persistence(39));
console.log(persistence(999));
console.log(persistence(4));