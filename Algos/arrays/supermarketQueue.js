// There is a queue for the self-checkout tills at the supermarket. 
// Your task is write a function to calculate the total time required for all the customers to check out!

/* 
Input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
*/

// Output: The function should return an integer, the total time required.

/* 
Clarifications:
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool
*/

// Not Done Yet

function queueTime(customers, n) {
    let totalTime = 0;
    let most = 0;
    let mostIdx = 0;
    for (let i = 0; i < customers.length; i++){
        if (n === 1){
        totalTime += customers[i];
        }
        else if (customers[i] > most){
            most = customers[i];
            mostIdx = i;
            continue;
        }
        if (customers[i] < most){
            totalTime += customers[i];
        }
    }
    if (n !== 1){
        totalTime += most;
    }
    return totalTime;
}

console.log(queueTime([5,3,4], 1));
console.log(queueTime([10,2,3,3], 2));
console.log(queueTime([2,3,10], 2));