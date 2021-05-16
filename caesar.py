
def encrypt(key,plaintext):
    ciphertext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for l in plaintext.upper():
        if l in alphabet:
            i = (alphabet.find(l) + key) % 26
            ciphertext = ciphertext + alphabet[i]
        else:
            ciphertext += l

    return ciphertext

def decrypt(key,ciphertext):
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for l in ciphertext.upper():
        if l in alphabet:
            i = (alphabet.find(l) - key) % 26
            plaintext = plaintext + alphabet[i]
        else:
            plaintext += l

    return plaintext


