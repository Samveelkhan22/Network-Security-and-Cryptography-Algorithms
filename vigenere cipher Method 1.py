def generate_vigenere_table():
    table = [[0] * 26 for _ in range(26)]
    for i in range(26):
        for j in range(26):
            table[i][j] = chr(((i+j)% 26) + 65)
    return table
def vigenere_encrypt(plain_text, key):
    cipher_text=''
    table= generate_vigenere_table()
    key = key.upper()
    plain_text = plain_text.upper()
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            cipher_text += table[ord(char) - 65][shift]
            key_index = (key_index + 1 )% len (key)
        else:
            cipher_text +=char
    return cipher_text
def vigenere_decrypt(cipher_text, key):
    plain_text =''
    table = generate_vigenere_table()
    key  = key.upper()
    cipher_text = cipher_text.upper()
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            shift = ord(key [key_index]) - 65
            for i in range(26):
                if table[i][shift] == char:
                    plain_text += chr (i +65)
                    break
            key_index = (key_index + 1)% len (key)
        else:
            plain_text +=char
    return plain_text
plain_text = "Sadaf Khan"
key ="LOCK"
encrypted_text = vigenere_encrypt(plain_text, key)
print("Encrypted:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
