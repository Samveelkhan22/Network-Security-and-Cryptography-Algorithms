def viginere_encrypt(palain_text,key):
    encrypted_text = ''
    key = key.upper()
    key_index = 0 
    for char in plain_text.upper():
        if char.isalpha():
            p = ord(char)-65
            k = ord(key[key_index]) - 65
            encrypted_char = chr(((p+k)% 26)+ 65)
            encrypted_text += encrypted_char
            key_index = (key_index +1 ) % len(key)
        else:
            encrypted_text += char
    return encrypted_text
def vigenere_decrypt( encrypted_text, key):
    decrypted_text=''
    key= key.upper()
    key_index = 0
    for char in encrypted_text.upper():
        if char.isalpha():
            e=  ord(char) - 65
            k = ord(key[key_index]) - 65
            decrypted_char = chr((( e-k) % 26) +65)
            decrypted_text += decrypted_char
            key_index =(key_index + 1) % len (key)
        else:
            decrypted_text += char
    return decrypted_text

plain_text = "She is listening"
key = "Pascal"
encrypted_text = viginere_encrypt(plain_text, key)
print("Encrypted:" , encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted", decrypted_text)
