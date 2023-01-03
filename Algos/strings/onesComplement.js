// The One's Complement of a binary number is the number obtained by swapping all the 0s for 1s and all the 1s for 0s.

// For any given binary number, formatted as a string, return the Ones' Complement of that number.

const onesComplement = n => {
    let result = "";
    for (let i = 0; i < n.length; i++){
        // console.log(`This is n[i]: ${n[i]}`);
        if (n[i] === '1') result += 0;
        else result += 1;
    }
    return result;
}

console.log(onesComplement('1001')) // 0110
