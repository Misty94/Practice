// Take any non-negative integer & return it with its digits in descending order.
// So, rearrange the digits to create the highest possible number.

const descendingOrder = num => {
    let sN = num.toString();
    let arr = sN.split(''); // Split the string into an array of characters
    arr.sort((a, b) => b - a); // Sort the array in descending order
    let result = arr.join(''); // Join the array back into a string
    return parseInt(result);
}

console.log(descendingOrder(58199)) // 99851
console.log(descendingOrder(367104)) // 764310



// *************************************************************************************

const explanation = n => {
    let strNum = n.toString();
    console.log("I changed the integer into a string. strNum = ", strNum); // strNum = 47253
    let arr = strNum.split('');
    console.log("This is what happened when I used the split method. arr = ", arr); // arr = [ '4', '7', '2', '5', '3' ]
    arr.sort((a, b) => b - a);
    // console.log("Then I sort the array into descending order. This is a and b: ", a, b); This did not work.
    let newNum = arr.join('');
    console.log("I then joined the array back into a string. So newNum is ", newNum); // newNum is 75432
    parseInt(newNum);
    console.log("Now, I changed the string back into an integer. This is the new integer: ", newNum); // newNum: 75432
    return newNum;
}

console.log(explanation(47253)) // 75432


// **********************************************************************************************

const bestPractice = (n) => {
    return parseInt(String(n).split('').sort().reverse().join(''));
}

console.log(bestPractice(502841)) // 854210


function dOrder(num) {
    return Number(num.toString().split('').sort((a,b) => b-a).join(''));
}

console.log(dOrder(21979)) // 99721