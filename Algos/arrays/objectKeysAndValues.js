// Create a function that takes an object & returns the keys and values as separate arrays.
// Return the keys sorted alphabetically & their corresponding values in the same order.

const keysAndValues = (obj) => {
    let resultKs = [];
    let resultVs = [];
    for (k of Object.keys(obj)){
        resultKs.push(k);
    }
    for (v of Object.values(obj)){
        resultVs.push(v);
    }
    return `[${resultKs}], [${resultVs}]`;
}

console.log(keysAndValues({ a: 1, b: 2, c: 3 }));
console.log(keysAndValues({ a: "Apple", b: "Microsoft", c: "Google" }));
console.log(keysAndValues({ key1: true, key2: false, key3: undefined }));
console.log(keysAndValues({ z: 50, y: 30, x: 100 })); // Figure out the alphabetical thing! (Maybe use sort() function)