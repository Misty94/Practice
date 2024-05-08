for (var x = 1; x < 9; x += 3){
    console.log(x);
}

// 1,4,7

var msg = 'codingdojo';
for(var x = 11; x < msg.length + 5; x += 3){
    console.log(x);
}

// 11,14

var x = 10;
if (x == 10){
    console.log(x);
} else {
    console.log('hello');
}

// 10

var message = 'dojo';
if (message == 'dojo'){
    console.log('coding'+message);
}
else {
    console.log('ninja'+message);
}

// codingdojo

for (var x = 20; x > 3; x-=2){
    console.log(x);
    break;
}

// 20

var msg = 'hello!';
for (var x = 15; x > msg.length + 8; x-=3){
    console.log(x);
}

// 15

var msg = 'codingdojo';
for (var x = -1; x < msg.length - 2; x+=2){
    if (msg.length == 8){
        console.log(i);
    } 
    else {
        for (var i = msg.length; i > (msg.length - 1); i-=3){
            console.log(i);
        }
    }
}

// 10,10,10,10,10

// Create a function that returns the sum of all odd numbers from 10 to 400

function sum_odd(){
    var sum = 0;
    for (var i = 10; i < 401; i++){
        if (i % 2 === 1){
            sum += i;
        }
    }
    return sum;
}

console.log(sum_odd());

// Create a function that will return the sum of all values in the array.

function sumOfArray(){
    var array = [-3, -55, 10, -19, 27, -6, 2, 0, -11, -4];
    var sum = 0;
    for (var i = 0; i < array.length; i++){
        sum += array[i];
    }
    return sum;
}

console.log(sumOfArray());

// Create a function that will return the average of all values in the array.

function averageOfArray(){
    var array = [4, 9, -23, 14, -6, 20, 33, -8, 1, -52];
    // var array = [95, 100, 100];
    var sum = 0;
    for (var i = 0; i < array.length; i++){
        sum += array[i];
    }
    return sum / array.length;
}

console.log(averageOfArray());