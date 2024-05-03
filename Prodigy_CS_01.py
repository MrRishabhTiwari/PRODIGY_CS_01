def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (positive integer): "))
    encrypted_message = caesar_encrypt(message, shift)
    print("Encrypted message:", encrypted_message)
if __name__ == "__main__":
    main()
