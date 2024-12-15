def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char)
            if char.islower():
                char_code += shift_amount
                if char_code > ord('z'):
                    char_code -= 26
            elif char.isupper():
                char_code += shift_amount
                if char_code > ord('Z'):
                    char_code -= 26
            encrypted_text += chr(char_code)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to encrypt or decrypt a message? (e/d): ").strip().lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        return
    
    message = input("Enter your message: ").strip()
    try:
        shift = int(input("Enter the shift value: ").strip())
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return
    
    if choice == 'e':
        result = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {result}")
    else:
        result = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
