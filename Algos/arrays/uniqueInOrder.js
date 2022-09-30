// Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

var uniqueInOrder=function(iterable){
    //your code here - remember iterable can be a string or an array
    let result = [];
    for (let i = 0; i < iterable.length; i++){
        if (iterable[i] !== iterable[i-1]){
            result.push(iterable[i])
        }
    }
    return result;
}

console.log(uniqueInOrder('AAAABBBCCDAABBB'));
console.log(uniqueInOrder('ABBCcAD'));
console.log(uniqueInOrder([1,2,2,3,3]));