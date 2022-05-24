
import random

character_pool = [
                ["A","B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], 
                ["a", 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                ["1","2","3","4","5","6","7","8","9","0"], 
                ["!", "?", "_", "."],
]

def randomizer():
    result = random.choice(character_pool)
    final = random.choice(result)
    return final
def generator(length):
    password_generator = []
    i = 0
    while i < length:
        password_generator.append(randomizer())
        i += 1
    password = ''.join(password_generator)
    
    print(f"{password}")
    return password
    

generator(13)
