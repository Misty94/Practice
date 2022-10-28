// ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

function validatePIN (pin) {
    //return true or false
    for (let i = 0; i < pin.length; i++){
        if (isNaN(pin[i]) || pin[i] === ' ' || pin[i] === '\n') return false;
    }
    if (pin.length === 4 || pin.length === 6) return true;
    return false;
}

console.log(validatePIN('1234'));
console.log(validatePIN('12345?'));
console.log(validatePIN('a234'));
console.log(validatePIN('123 '));
console.log(validatePIN('7234888'));
console.log(validatePIN('123b45'));
console.log(validatePIN('123925'));



// CodeWars Different Solutions:
const validatePIN2 = pin => /^(\d{4}$|\d{6}$)/.test(pin);

function validatePIN3 (pin) {
    var reg = new RegExp('^([0-9]{4}|[0-9]{6})$');
    return reg.test(pin);
}

console.log(validatePIN2('123b45'));
console.log(validatePIN3('123925'));