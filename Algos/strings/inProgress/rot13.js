// ROT13 is a letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.

// Input: a string 
// Output: the string ciphered with Rot13
// Considerations: if numbers or special characters present, they should remain where they are

const rot13 = message => {
    let alph = {
        "a": "n",
        "b": "o",
        "c": "p",
        "d": "q",
        "e": "r",
        "f": "s",
        "g": "t",
        "h": "u",
        "i": "v",
        "j": "w",
        "k": "x",
        "l": "y",
        "m": "z",
        "n": "a",
        "o": "b",
        "p": "c",
        "q": "d",
        "r": "e",
        "s": "f",
        "t": "g",
        "u": "h",
        "v": "i",
        "w": "j",
        "x": "k",
        "y": "l",
        "z": "m"
    }
    let code = '';
    // for (let i = 0; i < message.length; i++){
    //     for (let j = 0; j < alph.length; j++){
    //         if (message[i] === alph[i].key){
    //             code += alph[i].value;
    //         }
    //     }
    // }
    return code;
}

console.log(rot13("codewars"))