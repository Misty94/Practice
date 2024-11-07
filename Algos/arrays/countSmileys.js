// Given an array as an argument, return the total number of smiling faces.
// Smiling Faces must contain a valid pair of eyes meaning : or ;
// Smiling Faces doesn't have to but can have a nose meaning - or ~
// Smiling Faces must have a smiling mouth meaning ) or D

// No other characters are allowed!
// Valid Smiley Faces Examples:    :)   :D   ;-)   ;~D

// Note: In case of an empty array, return 0
// Note: Order of the face (eyes, nose, mouth) will always be the same

function countSmileys(arr) {
    if (arr.length === 0) return 0;
    let smileys = 0;
    for (let i = 0; i < arr.length; i++){
        // console.log("This is arr[i]: " + arr[i]);
        if (arr[i] === ':)' || arr[i] === ':D' || arr[i] === ';)' || arr[i] === ';D'){
            smileys++;
        }
        else if (arr[i] === ':-)' || arr[i] === ':-D' || arr[i] === ';-)' || arr[i] === ';-D'){
            smileys++;
        }
        else if (arr[i] === ':~)' || arr[i] === ':~D' || arr[i] === ';~)' || arr[i] === ';~D'){
            smileys++;
        }
        else continue;
    }
    return smileys;
}

console.log(countSmileys([])); // 0
console.log(countSmileys([':)', ';(', ';{'])); // 1
console.log(countSmileys([';~)', ';-(', ';)', ':-D'])); // 3
console.log(countSmileys([':D', ':~)', ';*', ':$'])); // 2

// ****************************************************************************************************************************

// Filter Option

function countSmileyFaces(arr) {
    return arr.filter(x => /^[:;][-~]?[)D]$/.test(x)).length;
}

console.log(countSmileyFaces([':O', ';~D', ':-D', ':)'])) // 3

// *****************************************************************************************************************************

// An Array of Acceptable Answers Option => But This Requires 2 For Loops

const countTheSmileys = arr => {
    let smileys = [':)', ';)', ':-)', ':~)', ';-)', ';~)', ':D', ';D', ':-D', ':~D', ';-D', ';~D'];
    let count = 0;
    for (let i = 0; i < arr.length; i++){
        for (let j = 0; j < smileys.length; j++){
            if (arr[i] === smileys[j]){
                count++;
            }
        }
    }
    return count;
}

console.log(countTheSmileys([';O', ';D', ':-D', ':-)', ':D', ':('])) // 4

// *****************************************************************************************************************************

// Another Way For Acceptable Answers without 2 For Loops

const smileyFaces = (arr) => {
    let smileys = 0;
    let smileyFaces = [':)', ';)', ':-)', ':~)', ';-)', ';~)', ':D', ';D', ':-D', ':~D', ';-D', ';~D'];
    for (let i = 0; i < arr.length; i++){
        if (smileyFaces.includes(arr[i])){
            smileys++;
        }
    }
    return smileys;
}

console.log(smileyFaces([':-D', ':(', ';$'])) // 1

// *****************************************************************************************************************************

// Another Way For Acceptable Answers using Filter

const numOfSmileys = (arr) => {
    const smileyFaces = [':)', ';)', ':-)', ':~)', ';-)', ';~)', ':D', ';D', ':-D', ':~D', ';-D', ';~D'];
    return arr.filter((smileys) => smileyFaces.includes(smileys)).length;
}

console.log(numOfSmileys([';{', ':}', ';D'])) // 1