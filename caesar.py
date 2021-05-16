
def encrypt(key,plaintext):
    plaintext = plaintext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""

    for l in plaintext:
        if l in alphabet:
            i = (alphabet.find(l) + key) % 26
            ciphertext = ciphertext + alphabet[i]
        else:
            ciphertext = ciphertext++

    return ciphertext

def decrypt(key,ciphertext):
    ciphertext = ciphertext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""

    for l in ciphertext:
        if l in alphabet:
            i = (alphabet.find(l) - key) % 26
            plaintext = plaintext + alphabet[i]
        else:
            plaintext = plaintext++

    return plaintext


