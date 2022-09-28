// Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

// In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

// More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

function DNAStrand(dna){
    let comp = "";
    for (let i = 0; i < dna.length; i++){
        if (dna[i] === 'A'){
            comp += 'T';
        }
        else if (dna[i] === 'T'){
            comp += 'A';
        }
        else if (dna[i] === 'C'){
            comp += 'G';
        }
        else if (dna[i] === 'G'){
            comp += 'C';
        }
    }
    return comp;
}

console.log(DNAStrand("ATTGC"));
console.log(DNAStrand("GTAT"));




// CodeWars Different Solutions:

function DNAStrand2(dna){
    var pairs = {'A':'T','T':'A','C':'G','G':'C'};
    return dna.split('').map(function(v){ return pairs[v] }).join('');
}

function DNAStrand3(dna){
    var table = {
        C : 'G',
        G : 'C',
        A : 'T',
        T : 'A'
    };

    return dna.split('').map(function(cv) {
        return table[cv]; 
    }).join('');
}

console.log(DNAStrand2("ATTGC"));
console.log(DNAStrand3("GTAT"));