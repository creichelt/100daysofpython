alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# final including not included characters and shift range limiting
def caesar(direction, text, shift):
    shift = shift % 26
    cipher_text = ''
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter in alphabet:
            cipher_text += alphabet[alphabet.index(letter) + shift]
        else:
            cipher_text += letter
    print(f"The {direction}d message is: {cipher_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction,text,shift)

    if input("Do you want to go again?").lower() == 'no':
        break


# # simplified:
# def caesar(direction, text, shift):
#     cipher_text = ''
#     if direction == 'decode':
#         shift *= -1
#     for letter in text:
#         cipher_text += alphabet[alphabet.index(letter) + shift]
#     print(f"The {direction}d message is: {cipher_text}")

## basic:
# def encrypt(text, shift):
#     cipher_text = ''
#     for letter in text:
#         # position = alphabet.index(letter) + shift
#         # letter = alphabet[position]
#         # cipher_text += letter
#         cipher_text += alphabet[alphabet.index(letter) + shift]
#     print(f"encoded message is: {cipher_text}")
#
# def decrypt(text, shift):
#     decipher_text = ''
#     for letter in text:
#         decipher_text += alphabet[alphabet.index(letter) - shift]
#     print(f"decoded message is: {decipher_text}")
#
# if direction == 'encode':
#     encrypt(text,shift)
# elif direction =='decode':
#     decrypt(text,shift)
