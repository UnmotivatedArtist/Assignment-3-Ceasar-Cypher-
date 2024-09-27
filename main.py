secret_message = "This is most deffinitely NOT a secret message 4 (p.s. vigenere ciphers are better)"
number = 12

def caesar_cipher(text: str, shift: int):
    result = ""

    for char in text:
        if char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)

        else:
            result += char

    return result

print(caesar_cipher(secret_message, number))



hidden_message = caesar_cipher(secret_message, number)



def caesar_decipher(text: str, shift: int):
    result = ""

    for char in text:
        if char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.isdigit():
            result += chr((ord(char) - shift - 48) % 10 + 48)

        else:
            result += char

    return result

print(caesar_decipher(hidden_message, number))
