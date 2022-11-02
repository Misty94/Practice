// Create function that takes a positive integer & rearrange its next digits to return a bigger number.

// Considerations: If the digits can't be rearranged to form a bigger number, return -1.

const nextBigger = n => {
    let sN = n.toString();
    let num = '';
    for (let i = 0; i < sN.length; i++){
        if (sN.length % 2 === 0){
            if (sN[i] > sN[i+1]){
                num += `${sN[i]}${sN[i+1]}`;
                i++;
            } else {
                num += `${sN[i+1]}${sN[i]}`;
                i++;
            }
        } else {
            if (sN[i] > sN[i+1]){
                num += `${sN[i]}`;
            } else {
                if (!sN[i+1]){
                    num += `${sN[i]}`;
                } else {
                    num += `${sN[i+1]}${sN[i]}`;
                    i++;
                }
            }
        }
    }
    let newNum = parseInt(num);
    if (newNum === n) return -1;
    else return newNum;
}


// It works for these, but codewars failed some random attempts.
console.log(nextBigger(12)); // 21
console.log(nextBigger(513)); // 531
console.log(nextBigger(2017)); // 2071
console.log(nextBigger(414)); // 441
console.log(nextBigger(144)); // 414
console.log(nextBigger(278232)); // ??



    // for (let i = 1; i < strN.length; i++){
    //     if (strN.length <= 3){
    //         if (strN[i] <= strN[i-1]){
    //             num += `${strN[i-1]}`;
    //         } else {
    //             num += `${strN[i]}${strN[i-1]}`;
    //         }
    //     } else {
    //         num += strN[0];
    //         console.log(`This is num: ${num}`)
    //         if (strN[i] <= num[i-1]){
    //             num += `${strN[i]}`;
    //         } else {
    //             let temp = num[i-1];
    //             console.log("This is temp: ", temp);
    //             num -= `${num[i-1]}`;
    //             num += `${strN[i]}${temp}`;
    //         }
            // if (strN[i] <= strN[i-1] && strN[i] <= strN[i+1]){
            //     num += `${strN[i-1]}${strN[i]}${strN[i+1]}`;
            //     i++;
            // }
            // else if (strN[i] > strN[i-1] && strN[i] <= strN[i+1]){
            //     num += `${strN[i]}${strN[i-1]}`;
            // }
            // else if (strN[i] > strN[i+1]){
            //     num += `${strN[i+1]}${strN[i]}`;
            //     i++;
            // }
    //     }
    // }