# PRODIGY_CS_01
Caesar Cipher Encryption:
The function caesar_encrypt(text, shift) takes two parameters: text, the message to be encrypted, and shift, the number of positions each letter in the message should be shifted in the alphabet.
It initializes an empty string encrypted_text to store the encrypted message.
It iterates through each character in the input text.
If the character is an alphabet letter (using char.isalpha()), it calculates the shifted position of the letter by adding the shift value to its Unicode value (ord(char)).
For lowercase and uppercase letters, it handles wrapping around the alphabet if the shifted position goes beyond 'z' or 'Z' respectively.
It appends the shifted character to the encrypted_text.
If the character is not an alphabet letter, it appends it unchanged to the encrypted_text.
Finally, it returns the encrypted_text.
Caesar Cipher Decryption:
The function caesar_decrypt(text, shift) simply calls caesar_encrypt with a negative shift value (-shift), effectively decrypting the message.
Usage:
In the main() function, it prompts the user to input a message and a shift value.
It calls caesar_encrypt with the provided message and shift value, and prints the encrypted message.
