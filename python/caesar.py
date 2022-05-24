import string
# alphabet = list(string.ascii_lowercase)
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !? ."

# First - Create new array with the rotated values:
def rot(key):
    newAlph = []
    for letter in symbols:
        index = (symbols.index(letter) + key) - 1
        # print(index)
        if(index >= len(symbols)):
            index = index - len(symbols)
            newAlph.append(symbols[index])
        else:
            newAlph.append(symbols[index])
    return newAlph

def encrypt(message):
    key = int(input(f"Enter key between 1-{len(symbols)}\n"))
    newAlphabet = rot(key)
    encrypted = []

    for char in message:
        letter = newAlphabet[symbols.index(char)]
        encrypted.append(letter)

    newMessage = ''.join(encrypted);

    print(newMessage)


message = input("Please enter a word to encrypt...\n")
encrypt(message)