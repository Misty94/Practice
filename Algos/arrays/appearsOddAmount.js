// Given an array of integers, find the one that appears an odd number of times.

// There will always be only one integer that appears an odd number of times.

function findOdd(A) {
    //happy coding!
    let count = 0;
    for (let i = 0; i < A.length; i++){
        let num = A[i];
        for (let j = 0; j < A.length; j++){
            if (A[j] === num){
                count++;
            }
        }
        if (count % 2 === 1){
            return num;
        } else {
            count = 0;
        }
    }
}

console.log(findOdd([1,1,2]));
console.log(findOdd([7]));
console.log(findOdd([1,2,2,3,3,3,4,3,3,3,2,2,1]));