def encrypt_caesar(plain_text, k):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            # Check if the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Convert the character to its corresponding position in the alphabet (0-25)
            char_position = ord(char.lower()) - ord('a')
            
            # Apply the Caesar Cipher encryption formula
            encrypted_position = (char_position + k) % 26
            
            # Convert the encrypted position back to the corresponding character
            encrypted_char = chr(encrypted_position + ord('a'))
            
            # Convert the character back to uppercase if it was originally uppercase
            if is_upper:
                encrypted_char = encrypted_char.upper()
            
            encrypted_text += encrypted_char
        else:
            # If the character is not an alphabet letter, leave it unchanged
            encrypted_text += char
    
    return encrypted_text

def decrypt_caesar(encrypted_text, k):
    # To decrypt, we use the same formula with a negative shift (k becomes -k)
    return encrypt_caesar(encrypted_text, -k)

# Example usage
plain_text = "samveel zaheer khan"
shift = 3
encrypted_text = encrypt_caesar(plain_text, shift)
decrypted_text = decrypt_caesar(encrypted_text, shift)

print("Original Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
