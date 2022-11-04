// Input: String of only digits (big numbers)
// Output: String of the sum of two numbers
// Considerations: The numbers are positive.

const addBigNumbers = (a, b) => {
    // return (Number(a) + Number(b)).toString(); // Fix me! <- This only handles smaller numbers.
    /* let aNum = parseInt(a);
    let bNum = parseInt(b);
    let sum = aNum + bNum; <- This also works, but not on the really big numbers.
    return sum.toString(); */
}

console.log(addBigNumbers("123", "321"));
console.log(addBigNumbers("11", "99"));
console.log(addBigNumbers('63829983432984289347293874', '90938498237058927340892374089')); // "91002328220491911630239667963"