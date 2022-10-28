// Output is total number of true in the array.
// Input is an array of true and false representing if sheep is present
// Constraints?? Check for edge cases like null or undefined. (an example of a constraint)
// Examples??

const countingSheep = arr => {
    let tCount = 0;
    for (let i = 0; i < arr.length; i++){
        if (arr[i] === true){
            tCount++;
        }
    }
    return tCount;
}

console.log(countingSheep([true,true,false,true,true,false,false,false,true,true,true,true,true,false]));




function sheepCounting(arr){
    return arr.filter(Boolean).length;
}

console.log(sheepCounting([true,true,false,true,true,false,false,false,true,true,true,true,true,false]));