// Take the num parameter being passed and return the factorial of it.

function FirstFactorial(num) { 

    // code goes here  
    let result = 1;
    for (let i = num; i > 0; i--){
        result *= i;
    }
    return result; 

}

console.log(FirstFactorial(8));