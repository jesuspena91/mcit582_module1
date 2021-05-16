
def encrypt(key,plaintext):
	ciphertext = ""
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper()

    for l in plaintext:
        if l in alphabet:
            i = (alphabet.find(l) + key) % 26
            ciphertext = ciphertext + alphabet[i]
        else:
            ciphertext += l

    return ciphertext

def decrypt(key,ciphertext):
	plaintext = ""
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper()

    for l in ciphertext:
        if l in alphabet:
            i = (alphabet.find(l) - key) % 26
            plaintext = plaintext + alphabet[i]
        else:
            plaintext += l

    return plaintext


