
def encrypt(key,plaintext):
    ciphertext=""
    message = plaintext.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            ciphertext = ciphertext + alpha[letter_index]
        else:
            ciphertext = ciphertext + letter

    return ciphertext

def decrypt(key,ciphertext):
    message = ciphertext.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            plaintext = plaintext + alpha[letter_index]
        else:
            plaintext = plaintext + letter

    return plaintext


