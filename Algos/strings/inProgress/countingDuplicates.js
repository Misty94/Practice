// Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
// The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

const duplicateCount = text => {
    // let count = 0;
    // let totalCount = 0;
    // let duplicate = '';
    // let x = 0;
    // duplicate += text[0];
    // for (let i = 1; i < text.length; i+2){
    //     for (let j = i+1; j < text.length; j++){
    //         if (text[i] === duplicate[x]){
    //             continue;
    //         }
    //         if (text[i] === text[j] || text[i] === text[j].toUpperCase() || text[i] === text[j].toLowerCase()){
    //             count++;
    //             duplicate += text[i];
    //             if (duplicate.length > 1){
    //                 x++;
    //             }
    //         }
    //     }
    //     if (count > 0){
    //         totalCount++;
    //         count = 0;
    //     }
    // }
    // return totalCount;
}

console.log(duplicateCount("invisibility"));
console.log(duplicateCount("invisibilities"));