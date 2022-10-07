// Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

// HH = hours, padded to 2 digits, range: 00 - 99
// MM = minutes, padded to 2 digits, range: 00 - 59
// SS = seconds, padded to 2 digits, range: 00 - 59
// The maximum time never exceeds 359999 (99:59:59)

const humanReadable = seconds => {
    let time = '';
    
}



console.log(humanReadable("9"));
console.log(humanReadable("59"));
console.log(humanReadable("60"));
console.log(humanReadable("90"));
// console.log(humanReadable("3599"));


/*
    let time = '';
    for (let i = seconds.length-1; i >= 0; i--){
        if (seconds.length === 1){
            time += `00:00:0${seconds[i]}`
        }
    }
    ****************************
    return time;
    let time = '';
    let temp = 0;
    if (seconds.length === 1) return `00:00:0${seconds}`;
    if (seconds.length === 2){
        time = `00:00:0${seconds[1]}`;
        if (seconds[0] <= 5){
            time = `00:00:${seconds[0]}${seconds[1]}`;
        } else {
            temp = seconds[0] - 5;
            time = `00:0${temp}:0${seconds[1]}`;
        }
    }
    return time;
*/