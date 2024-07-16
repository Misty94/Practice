const openLogin = () => {
    document.getElementById("loginForm").style.display = "block";
    console.log("HELLLLOOOOOOOO")
}

const openReg = () => {
    document.getElementById("regForm").style.display = "block";
    console.log("regggggg")
}

const openComment = () => {
    document.getElementById("commentForm").style.display = "block";
    console.log("Comment was left.")
}

function closeLogin() {
    document.getElementById("loginForm").style.display = "none";
}

function closeReg() {
    document.getElementById("regForm").style.display = "none";
}

function closeComment() {
    document.getElementById("commentForm").style.display = "none";
}

const generateQuotes = function() {
    const quotes = [
        {
            quote: "What sculpture is to a block of marble, education is to a human soul.",
            author: "Joseph Addison"
        },
        {
            quote: "Education is the most powerful weapon which you can use to change the world.",
            author: "Nelson Mandela"
        },
        {
            quote: "Children must be taught how to think, not what to think.",
            author: "Margaret Mead"
        },
        {
            quote: "Every child deserves a champion—an adult who will never give up on them, who understands the power of connection and insists that they become the best that they can possibly be.",
            author: "Rita Pierson"
        },
        {
            quote: "The art of teaching is the art of assisting discovery.",
            author: "Mark Van Doren"
        },
        {
            quote: "Education breeds confidence. Confidence breeds hope. Hope breeds peace.",
            author: "Confucius"
        },
        {
            quote: "Teaching is the one profession that creates all other professions.",
            author: "Unknown"
        },
        {
            quote: "If you are planning for a year, sow rice; if you are planning for a decade, plant trees; if you are planning for a lifetime, educate people.",
            author: "Chinese Proverb"
        },
        {
            quote: "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
            author: "Benjamin Franklin"
        },
        {
            quote: "I cannot teach anybody anything; I can only make them think.",
            author: "Socrates"
        },
        {
            quote: "Better than a thousand days of diligent study is one day with a great teacher.",
            author: "Japanese Proverb"
        },
        {
            quote: "A good teacher is like a candle — it consumes itself to light the way for others.",
            author: "Mustafa Kemal Atatürk"
        },
        {
            quote: "Education is not the filling of a pail but the lighting of a fire.",
            author: "William Butler Yeats"
        },
        {
            quote: "Teaching is more than imparting knowledge; it is inspiring change. Learning is more than absorbing facts; it is acquiring understanding.",
            author: "William Arthur Ward"
        },
        {
            quote: "What we want is to see the child in pursuit of knowledge, and not knowledge in pursuit of the child.",
            author: "George Bernard Shaw"
        },
        {
            quote: "Students don’t care how much you know until they know how much you care.",
            author: "Anonymous"
        }
    ];

    let arrayIndex = Math.floor(Math.random() * quotes.length);
    document.getElementById("quote").innerHTML = quotes[arrayIndex].quote;
    document.getElementById("author").innerHTML = quotes[arrayIndex].author;

}

window.onload = function() {
    generateQuotes();
    document.getElementById("generate").addEventListener('click', generateQuotes);
}