# Different cyphers

# Caesar cypher
def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = " "
    for char in text:
        if char == " ":
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text

# Vigenere cypher
def vigenere(text, key, direction = 1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ""

    for char in text:

        #Append any non-letter character
        if not char.isalpha():
            encrypted_text += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.index(char)
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text