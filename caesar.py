
def encrypt(key,plaintext):
    ciphertext=""

    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            ciphertext += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            ciphertext += chr((ord(char) + s - 97) % 26 + 97)
 
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    return plaintext


