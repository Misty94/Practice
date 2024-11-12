// Create a function that determines if all elements of a list are equal.
// The list can be a string or an array & return value is a boolean.

const allEqual = (myList) => {
    let first = myList[0];
    for (let i = 1; i < myList.length; i++){
        if (myList[i] !== first) return false;
    }
    return true;
}

console.log(allEqual([0,0,0])) // true
console.log(allEqual("aaaaa")) // true
console.log(allEqual("ab14")) // false
console.log(allEqual(["o", "o", "o", "o"])) // true
console.log(allEqual([2,2,2,2,8])) // false
