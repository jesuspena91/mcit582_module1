
def encrypt(key,plaintext):
	ciphertext = ""
    plaintext = plaintext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for l in plaintext:
        if l in alphabet:
            i = (alphabet.find(l) + key) % 26
            ciphertext = ciphertext + alphabet[i]
        else:
            ciphertext += l

    return ciphertext

def decrypt(key,ciphertext):
	plaintext = ""
    ciphertext = ciphertext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for l in ciphertext:
        if l in alphabet:
            i = (alphabet.find(l) - key) % 26
            plaintext = plaintext + alphabet[i]
        else:
            plaintext += l

    return plaintext


