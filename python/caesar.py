import string
alphabet = list(string.ascii_lowercase)

# # Second - Use that new array to 'encrypt':
# def encrypt(message):
#     rotation = int(input("Enter rotation between 1-25\n"))
#     newAlphabet = rot(rotation)

#     for char in message:
#         if char in alphabet:
#             print(char)


# encrypt("hi");


# First - Create new array with the rotated values:
def rot(rot):
    newAlph = []
    for letter in alphabet:
        index = (alphabet.index(letter) + rot) - 1
        # print(index)
        if(index >= 26):
            index = index - 26
            newAlph.append(alphabet[index])
        else:
            newAlph.append(alphabet[index])
    return newAlph

def encrypt(message):
    rotation = int(input("Enter rotation between 1-25\n"))
    newAlphabet = rot(rotation)

    encrypted = []

    for char in message:
        letter = newAlphabet[alphabet.index(char)]
        encrypted.append(letter)

    newMessage = ''.join(encrypted);

    print(newMessage)
encrypt("ezra")