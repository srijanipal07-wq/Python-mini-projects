# Text Encrypted And Decrypted Tool using string and user defined functions
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)
# Taking input from the user
text = input("Enter text: ")
key = int(input("Enter key: "))

# Encryption
encrypted = encrypt(text, key)
print("Encrypted text:", encrypted)

# Decryption
decrypted = decrypt(encrypted, key)
print("Decrypted text:", decrypted)