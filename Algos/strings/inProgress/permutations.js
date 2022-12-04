// Input: a non-empty string
// Output: an array of all possible permutations / shuffle all letters in all possible orders
// Considerations: remove any duplicates, if present

const permutations = string => {
    let result = [];
    let newSt = '';
    let ex = string;
    result.push(string);
    if (string.length === 1) return result;
    for (let i = 0; i < string.length; i++){
        newSt += string[i];
    }
    result.push(newSt);
    return result;
}

console.log(permutations("ab"))

/*  Examples:
* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
*/