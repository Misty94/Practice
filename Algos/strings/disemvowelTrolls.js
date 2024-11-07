// Trolls are attacking your comment section!
// A common way to deal with this situation is to remove all the vowels from the trolls' comments.
// Write a function that takes a string & return a new string with all the vowels removed.

// Note: For this, y is not considered a vowel

const disemvowel = str => {
    // let vowels = ['a', 'e', 'i', 'o', 'u']; // I think that would require 2 for loops
    let noVowels = '';
    for (let i = 0; i < str.length; i++){
        if (str[i] === 'a' || str[i] === 'e' || str[i] === 'i' || str[i] === 'o' || str[i] === 'u') continue;
        else if (str[i] === 'A' || str[i] === 'E' || str[i] === 'I' || str[i] === 'O' || str[i] === 'U') continue;
        else noVowels += str[i];
    }
    return noVowels;
}

console.log(disemvowel("This website is for losers LOL!")) // Ths wbst s fr lsrs LL!
console.log(disemvowel("I am a troll & this website sucks!")) // m trll & ths wbst scks!

// ************************************************************************************************************************

const noVowels = str => {
    return str.replace(/[aeiouAEIOU]/g, '');
}

console.log(noVowels("You suck and you're stupid!")) // Y sck nd y'r stpd!