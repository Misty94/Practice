function FirstReverse(str) { 

    // code goes here  
    let result = "";
    for (let i = str.length-1; i >= 0; i--){
        result += str[i]
    }
    return result; 

}

  // keep this function call here 
console.log(FirstReverse("I Love Code"));



// A Different Way Using Built In Methods
function FirstReverse2(string) {
    return string.split('').reverse().join('');
}

  // keep this function call here 
console.log(FirstReverse2("Welcome Misty"));