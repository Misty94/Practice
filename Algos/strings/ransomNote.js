/* 
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
*/

/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */


// var canConstruct = function (ransomNote, magazine) {
    // for (let i = 0; i < ransomNote.length; i++){
    //     for (let j = 0; j < ransomNote.length; j++){
    //         if (ransomNote[j] === magazine[i]) continue;
    //         else return false;
    //     }
    // }
    // return true;
    
// };

const canConstruct2 = (ransomNote, magazine) => {
    const v = magazine.split(''); //array of letters from magazine
    // console.log(v);
    
    for(let i = 0; i < ransomNote.length; i++){
        if(!v.includes(ransomNote[i])){ //if array doesnt have current letter, return false
            return false
        }
        
        const index = v.indexOf(ransomNote[i])
        v.splice(index,1) //if array does include, then we remove that element from the array so it cant be used twice
        console.log(v);
    }
    return true
}

console.log(canConstruct2("a", "b"));
console.log(canConstruct2("aa", "ab"));
console.log(canConstruct2("aa", "aab"));
console.log(canConstruct2("racecar", "rracaec"));