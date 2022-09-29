function printerError(s) {
    // let correct = 'abcdefghijklm';
    let incorrect = 'nopqrstuvwxyz';
    let count = 0;
    for (let i = 0; i < s.length; i++){
        for (let j = 0; j < 13; j++){
            if (s[i] === incorrect[j]){
                count++;
            }
        }
    }
    return `${count}/${s.length}`;
}


console.log(printerError('aaabzzzbbbbaijjm'));
console.log(printerError('nopjik'));


// CodeWars Different Solution:
function printerError2(s) {
    let allowedletters = ['a', 'b', 'c' ,'d' ,'e','f','g','h','i','j','k','l','m'];
    let errors = 0;
    for (x of s){
        if (!allowedletters.includes(x)) errors++;
    }
    return `${errors}/${s.length}`
}

console.log(printerError2('aaabzzzbbbbaijjm'));
console.log(printerError2('nopjik'));