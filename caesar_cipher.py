def caesar_cipher(text: str, shift: int, mode: str = "encrypt") -> str:
    """
    Encrypts or decrypts text using Caesar Cipher.
    mode: "encrypt" or "decrypt"
    """
    if mode == "decrypt":
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            # Preserve case
            base = ord('A') if char.isupper() else ord('a')
            # Shift within 0–25 then convert back to character
            offset = (ord(char) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            # Non-letters are kept as-is
            result.append(char)

    return "".join(result)


def main():
    print("=== Caesar Cipher ===")
    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for shift.")

    while True:
        print("\nChoose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            encrypted = caesar_cipher(message, shift, mode="encrypt")
            print(f"\nEncrypted message: {encrypted}")
            break
        elif choice == "2":
            decrypted = caesar_cipher(message, shift, mode="decrypt")
            print(f"\nDecrypted message: {decrypted}")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()