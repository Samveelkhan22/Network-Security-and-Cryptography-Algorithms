def encryptMorseCode(text):
    morseCode = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
    }
    text = text.upper()
    encodedText = ''
    for char in text:
        if char in morseCode:
            encodedText += morseCode[char] + ' '
        else:
            encodedText += char
    return encodedText.strip()

def decryptMorseCode(morseCode):
    morseToText = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
        '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' ', '': ''
    }
    morseWords = morseCode.strip().split(' ')
    decodedText = ''
    for word in morseWords:
        if word in morseToText:
            decodedText += morseToText[word]
        else:
            decodedText += ''
    return decodedText

text = "Sadaf Khan "
encryptedText = encryptMorseCode(text)
print("Original Text:", text)
print("Encrypted Text:", encryptedText)
decryptedText = decryptMorseCode(encryptedText)
print("Decrypted Text:", decryptedText)
