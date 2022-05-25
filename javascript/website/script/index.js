const character_pool = [
    ["A","B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], 
    ["a", 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    ["1","2","3","4","5","6","7","8","9","0"], 
    ["!", "?", "_", ".", "#", "@", "$","-"],
]
function randomizer(){
    let salt = Math.floor(Math.random() * character_pool.length);
    let salted = character_pool[salt];
    let shake = Math.floor(Math.random() * salted.length);
    let shook = salted[shake]
    
    return shook;
}

function generate(){
    const passwordArray = [];
    let i = 0;
    while (i < 14){
        passwordArray.push(randomizer());
        i++;
    }
    let password = passwordArray.join("");
    console.log(password)
}
