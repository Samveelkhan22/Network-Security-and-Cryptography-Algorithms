def encrypt_rail_fence(plain_text, rails):
    # Create a matrix to store the cipher text
    cipher_matrix = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
    
    # Variables to track the direction and position
    row, col = 0, 0
    down = False
    
    # Populate the matrix with the plain text
    for char in plain_text:
        if row == 0 or row == rails - 1:
            down = not down
        cipher_matrix[row][col] = char
        col += 1
        
        # Move to the next row based on the direction
        if down:
            row += 1
        else:
            row -= 1
            
    # Construct the cipher text from the matrix
    cipher_text = ''
    for i in range(rails):
        for j in range(len(plain_text)):
            if cipher_matrix[i][j] != '\n':
                cipher_text += cipher_matrix[i][j]
                
    return cipher_text

def decrypt_rail_fence(cipher_text, rails):
    # Create a matrix to store the cipher text
    plain_matrix = [['\n' for _ in range(len(cipher_text))] for _ in range(rails)]
    
    # Variables to track the direction and position
    row, col = 0, 0
    down = None
    
    # Populate the matrix with placeholders
    for _ in range(len(cipher_text)):
        if row == 0:
            down = True
        if row == rails - 1:
            down = False
        plain_matrix[row][col] = '*'
        col += 1
        if down:
            row += 1
        else:
            row -= 1
            
    # Fill the matrix with the cipher text
    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if (plain_matrix[i][j] == '*') and (index < len(cipher_text)):
                plain_matrix[i][j] = cipher_text[index]
                index += 1
    
    # Construct the plain text from the matrix
    row, col = 0, 0
    result = ''
    for _ in range(len(cipher_text)):
        if row == 0:
            down = True
        if row == rails - 1:
            down = False
        if plain_matrix[row][col] != '*':
            result += plain_matrix[row][col]
            col += 1
        if down:
            row += 1
        else:
            row -= 1
            
    return result

# Example usage
plain_text = "Mynameissamveel"
rails = 3
encrypted_text = encrypt_rail_fence(plain_text, rails)
decrypted_text = decrypt_rail_fence(encrypted_text, rails)

print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
