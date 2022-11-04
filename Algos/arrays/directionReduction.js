const dirReduc = arr => {
    let attempt = [];
    let finished = [];
    for (let i = 0; i < arr.length; i++){
        if (arr[i] === "NORTH" && arr[i+1] !== "SOUTH"){
            attempt.push(arr[i]);
        }
        else if (arr[i] === "SOUTH" && arr[i-1] !== "NORTH"){
            attempt.push(arr[i]);
        }
        else if (arr[i] === "EAST" && arr[i+1] !== "WEST"){
            attempt.push(arr[i]);
        }
        else if (arr[i] === "WEST" && arr[i-1] !== "EAST"){
            attempt.push(arr[i]);
        }
    }
    for (let j = 0; j < attempt.length; j++){
        if (attempt[j] === "NORTH" && attempt[j+1] !== "SOUTH" && attempt[j-1] !== "SOUTH"){
            finished.push(attempt[j]);
        }
        else if (attempt[j] === "SOUTH" && attempt[j-1] !== "NORTH" && attempt[j+1] !== "NORTH"){
            finished.push(attempt[j]);
        }
        else if (attempt[j] === "EAST" && attempt[j+1] !== "WEST" && attempt[j-1] !== "WEST"){
            finished.push(attempt[j]);
        }
        else if (attempt[j] === "WEST" && attempt[j-1] !== "EAST" && attempt[j+1] !== "EAST"){
            finished.push(attempt[j]);
        }
    }
    return finished;
}

console.log(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])); // WEST
console.log(dirReduc(["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"])); // EAST, NORTH
console.log(dirReduc(["SOUTH", "NORTH", "WEST", "EAST", "NORTH", "SOUTH", "WEST", "NORTH", "EAST", "WEST", "SOUTH", "NORTH", "WEST", "EAST"])); // WEST, NORTH