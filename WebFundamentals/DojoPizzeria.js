function pizzaOven(crustType, sauceType, cheeses, toppings){
    let pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

let pizza1 = pizzaOven("deep dish", "traditional", ["mozzerella"], ["pepperoni", "sausage"]);
console.log(pizza1);

let pizza2 = pizzaOven("hand tossed", "marinara", ["mozzerella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(pizza2);

let pizza3 = pizzaOven("pan", "marinara", ["mozzerella", "parmesan"], ["green peppers", "onions"]);
console.log(pizza3);

let pizza4 = pizzaOven("thin", "marinara", ["mozzerella", "cheddar"], ["pepperoni", "pineapple", "onions"]);
console.log(pizza4);


// Bonus: Create a Random Pizza

let crustTypes = ["deep dish", "hand tossed", "pan", "thin", "stuffed crust"];
let sauceTypes = ["traditional", "marinara", "bbq", "white sauce"];
let cheeseTypes = ["mozzarella", "cheddar", "parmesan", "feta", "swiss cheese"];
let toppingTypes = ["pepperoni", "onions", "green peppers", "pineapple", "mushrooms", "olives", "sausage", "chicken"];

function randomPick(arr){
    let i = Math.floor(arr.length * Math.random());
    return arr[i];
}

function randomRange(max, min){
    return Math.floor(Math.random() * max - min) + min;
}

function randomPizza(){
    let pizza = {};
    pizza.crustTypes = randomPick(crustTypes);
    pizza.sauceTypes = randomPick(sauceTypes);
    pizza.cheeseTypes = [];
    pizza.toppingTypes = [];
    for (let i = 0; i < randomRange(5, 1); i++){
        pizza.cheeseTypes.push(randomPick(cheeseTypes));
    }
    for (let j = 0; j < randomRange(4, 0); j++){
        pizza.toppingTypes.push(randomPick(toppingTypes));
    }
    return pizza;
}

console.log(randomPizza());