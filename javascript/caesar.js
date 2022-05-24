const alphabet = ["a", "b", "c", "d","e", "f", "g", "h","i", "j", "k", "l","m", "n", "o", "p","q", "r", "s", "t","u", "v", "w", "x","y", "z"]

function rot(rot){
    const newAlph = []
    for(let i = 0; i < alphabet.length; i++){
        let index = (i + rot) - 1
        if(index >= 26){
            index = index - 26
            newAlph.push(alphabet[index])
        }else{
            newAlph.push(alphabet[index])
        }
    }
    return newAlph;
}

function encrypt(message, rotation){
    const newAlph = rot(rotation);
    const encrypted = [];

    message.split("").forEach(char => {
        encrypted.push(newAlph[alphabet.indexOf(char)])
    });
    return encrypted.join("")
}

encrypt('ezra', 5)