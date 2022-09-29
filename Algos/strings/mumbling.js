function accum(s) {
	let newS = "";
    newS += s[0].toUpperCase();
    newS += "-";
    for (let i = 1; i < s.length; i++){
        newS += s[i].toUpperCase();
        for (let j = i; j > 0; j--){
            newS += s[i].toLowerCase();
        }
        if (i < s.length-1){
            newS += "-";
        }
    }
    return newS;
}

console.log(accum("abcd"));
console.log(accum("cwAt"));
console.log(accum("RqaEzty"));


// CodeWars Different Solution:
function accum2(s) {
    return s.split('').map((c, i) => (c.toUpperCase() + c.toLowerCase().repeat(i))).join('-');
}

console.log(accum2("abcd"));
console.log(accum2("cwAt"));
console.log(accum2("RqaEzty"));