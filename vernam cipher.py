def vernam_cipher(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        # Convert characters to numerical values (0-25 for alphabet)
        text_num = ord(text[i].upper()) - ord('A')
        key_num = ord(key[i % len(key)].upper()) - ord('A')

        # Perform XOR operation and ensure result stays within 0-25 range
        encrypted_num = (text_num + key_num) % 26

        # Convert back to character representation
        encrypted_text += chr(encrypted_num + ord('A'))
    return encrypted_text

def vernam_decipher(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        # Convert characters to numerical values (0-25 for alphabet)
        encrypted_num = ord(encrypted_text[i].upper()) - ord('A')
        key_num = ord(key[i % len(key)].upper()) - ord('A')

        # Perform XOR operation and ensure result stays within 0-25 range
        decrypted_num = (encrypted_num - key_num) % 26

        # Convert back to character representation
        decrypted_text += chr(decrypted_num + ord('A'))
    return decrypted_text

# Input from user
text = input("Enter the text to encrypt: ")
key = input("Enter the key: ")

# Encryption
encrypted_text = vernam_cipher(text, key)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = vernam_decipher(encrypted_text, key)
print("Decrypted:", decrypted_text)
