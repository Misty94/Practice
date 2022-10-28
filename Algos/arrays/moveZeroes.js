// Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

// moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

const moveZeros = (arr) => {
    let result = [];
    let count = 0;
    for (let i = 0; i < arr.length; i++){
        if (arr[i] !== 0){
            result.push(arr[i]);
        } else {
            count++;
        }
    }
    for (let j = 1; j <= count; j++){
        result.push(0);
    }
    return result;
}

console.log(moveZeros([false,1,0,1,2,0,1,3,"a"]));


// Veronica's Solution:

function zeroesEnd(arr){
    // Create a new array with NO zeroes using the filter method
    const noZero = arr.filter(a => a !== 0); // CallBack functions take care of your for loops - it does a specific task
    // Compare the lengths of the arr and the nonzero array to see how many we need to pad at the end
    let zeroArr = new Array(arr.length - noZero.length).fill(0);
    // We have the array with everything and then the zeroes 
    return noZero.concat(zeroArr);
}

console.log(zeroesEnd([false,1,0,1,2,0,1,3,"a"]));