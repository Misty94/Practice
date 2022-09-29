// Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

// The returned format must be correct in order to complete this challenge.

// Don't forget the space after the closing parentheses!

// function createPhoneNumber(numbers){
// }

const createPhoneNumber = (numbers) => {
    let phNum = "(";
    for (let i = 0; i < numbers.length; i++){
        if (i < 3){
            phNum += numbers[i];
            if (i === 2){
                phNum += ") ";
            }
        }
        else if (i < 6){
            phNum += numbers[i];
            if (i === 5){
                phNum += '-';
            }
        }
        else if (i < 10){
            phNum += numbers[i];
        }
    }
    return phNum;
}

console.log(createPhoneNumber([1,2,3,4,5,6,7,8,9,0]));
console.log(createPhoneNumber([2,8,6,5,4,1,0,3,2,7]));


// CodeWars Different Solution: 
function createPhoneNumber2(numbers){
    var format = "(xxx) xxx-xxxx";
    
    for(var i = 0; i < numbers.length; i++)
    {
        format = format.replace('x', numbers[i]);
    }
    
    return format;
}

console.log(createPhoneNumber2([1,2,3,4,5,6,7,8,9,0]));
console.log(createPhoneNumber2([2,8,6,5,4,1,0,3,2,7]));