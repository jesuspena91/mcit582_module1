
def encrypt(key,plaintext):
    plaintext = plaintext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""

    for letter in plaintext:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) + key) % 26
            ciphertext = ciphertext + alphabet[letter_index]
        else:
            ciphertext = ciphertext + letter

    return ciphertext

def decrypt(key,ciphertext):
    ciphertext = ciphertext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""

    for letter in ciphertext:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) - key) % 26
            plaintext = plaintext + alphabet[letter_index]
        else:
            plaintext = plaintext + letter

    return plaintext


