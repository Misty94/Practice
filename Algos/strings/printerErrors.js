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