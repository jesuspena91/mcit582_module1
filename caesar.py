
def encrypt(key,plaintext):
    plaintext = plaintext.upper()
    ciphertext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for l in plaintext:
        if l in alphabet:
            i = (alphabet.find(l) + key) % 26
            ciphertext = ciphertext + alphabet[i]
        else:
            ciphertext += l

    return ciphertext

def decrypt(key,ciphertext):
    ciphertext = ciphertext.upper()
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for l in ciphertext:
        if l in alphabet:
            i = (alphabet.find(l) - key) % 26
            plaintext = plaintext + alphabet[i]
        else:
            plaintext += l

    return plaintext


