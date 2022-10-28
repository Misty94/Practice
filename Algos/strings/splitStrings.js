// Split the string into pairs of 2 characters.
// If there is an odd number of characters, use an underscore _ to replace missing 2nd character.

const splitString = str => {
    let result = [];
    let i = 0;
    if (str.length === 0) return result;
    while (i < str.length-2){
        result.push(`${str[i]}${str[i+1]}`);
        i += 2;
    }
    if (str.length % 2 === 0){
        result.push(`${str[str.length-2]}${str[str.length-1]}`);
    } 
    else {
        result.push(`${str[str.length-1]}_`);
    }
    return result;
}

console.log(splitString("abcdef"));
console.log(splitString("abcdefg"));
console.log(splitString("abc"));
console.log(splitString(""));


// This worked on VS Code, but codewars failed it because it wanted an actual array.

// const splitString = str => {
//     let result = '[';
//     let i = 0;
//     while (i < str.length-2){
//         result += `'${str[i]}${str[i+1]}', `;
//         i += 2;
//     }
//     if (str.length % 2 === 0){
//         result += `'${str[str.length-2]}${str[str.length-1]}']`
//     } 
//     else {
//         result += `'${str[str.length-1]}_']`;
//     }
//     return result;
// }