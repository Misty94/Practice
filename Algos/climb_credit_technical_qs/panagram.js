// Panagram is the string that contains all 26 letters of the alphabet (irrespective of the case).

/* Input
The first line takes the input t denoting the number of testcases.
The following t lines takes the input for each of the corresponding strings.
*/

// Output: Print YES if the string is a panagram and NO if it is not

/*
abcdefghijkcflmnopqrscceftuvwrcrevrejnvibyz --- YES
ecedccnecrekcercervcerv --- NO
*/

const panagram = (t) => {
    let alpha = "abcdefghijklmnopqrstuvwxyz";
    for (let i = 0; i < t.length; i++){
        for (let y = 0; y < alpha.length; y++){
            console.log(t[i]);
            if (t[i] === alpha[y]) continue;
            else return "NO";
        }
    }
    return "YES";
}

console.log(panagram("abcdefghijkcflmnopqrscceftuvwrcrevrejnvibyz"));
console.log(panagram("ecedccnecrekcercervcerv"));