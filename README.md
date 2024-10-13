# Network Security and Cryptography Algorithms

This repository contains Python implementations of several classical cryptographic algorithms and models related to network security. Each algorithm demonstrates fundamental concepts used in secure communication and data protection. The repository is a valuable resource for those studying network security, cryptography, and information security.

## Table of Contents
- [Overview](#overview)
- [Implemented Algorithms](#implemented-algorithms)
  - [AES](#aes)
  - [Caeser Cipher](#caeser-cipher)
  - [Columnar Cipher](#columnar-cipher)
  - [Morse Code](#morse-code)
  - [Playfair Cipher](#playfair-cipher)
  - [Railfence Cipher](#railfence-cipher)
  - [Stream Cipher](#stream-cipher)
  - [Vernam Cipher](#vernam-cipher)
  - [Vigenere Cipher (Method 1)](#vigenere-cipher-method-1)
  - [Vigenere Cipher (Method 2)](#vigenere-cipher-method-2)
- [Usage](#usage)
- [Requirements](#requirements)

## Overview
Cryptography plays a crucial role in securing communications by transforming readable information into an unreadable format that can only be reverted to its original form by authorized parties. This project covers Python implementations of both traditional and widely used cryptographic techniques in network security.

## Implemented Algorithms

### AES (Advanced Encryption Standard)
AES is a symmetric block cipher that encrypts data in fixed-size blocks (128, 192, or 256 bits). It is widely used for secure communications and data protection.

### Caeser Cipher
A simple substitution cipher where each letter in the plaintext is shifted by a certain number of positions down or up the alphabet. This implementation supports both encryption and decryption functionalities.

### Columnar Cipher
A transposition cipher where the message is written in rows, and the ciphertext is formed by reading the columns. This method enhances the security of a message by permuting the characters.

### Morse Code
A representation of letters and numbers using dots and dashes. This implementation converts a message into Morse code and can also decode a Morse code message back into text.

### Playfair Cipher
A digraph substitution cipher, where pairs of letters are encrypted using a 5x5 matrix generated by a keyword. This algorithm improves security over simpler ciphers like the Caesar Cipher.

### Railfence Cipher
A transposition cipher where plaintext is written in a zigzag pattern (across multiple rows), and the ciphertext is read row by row. It is a simple yet effective way to scramble a message.

### Stream Cipher
A symmetric cipher that encrypts each bit or byte of data one at a time, typically using a pseudorandom key stream. It is ideal for scenarios where data needs to be encrypted on the fly, such as secure communication channels.

### Vernam Cipher
A cipher based on the principle of XORing the plaintext with a random key (one-time pad). It is theoretically unbreakable when used with a key of the same length as the plaintext and only used once.

### Vigenere Cipher (Method 1)
A polyalphabetic substitution cipher where the plaintext is encrypted using a key that repeats over the length of the message. Method 1 uses the basic Vigenere encryption technique where the key is repeated as needed.

### Vigenere Cipher (Method 2)
A variation of the Vigenere Cipher that adds an extra layer of security by dynamically modifying the key throughout the encryption process based on previous ciphertext characters.

## Usage
To use any of the provided scripts, simply run the corresponding Python file and follow the instructions in the terminal to input the text or ciphertext to be encrypted/decrypted.

## Requirements
- Python 3.12.1
