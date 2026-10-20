import os
from cryptography.fernet import Fernet, InvalidToken

KEY_FILE = "secret.key"


def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print(f"New key created and saved to '{KEY_FILE}'. Keep it safe, you need it to decrypt.")
    return key


def read_file(filename):
    try:
        with open(filename, "rb") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
    return None


def encrypt_file(filename):
    data = read_file(filename)
    if data is None:
        return
    key = load_or_create_key()
    encrypted = Fernet(key).encrypt(data)
    output_name = filename + ".enc"
    with open(output_name, "wb") as file:
        file.write(encrypted)
    print(f"Encrypted file saved as '{output_name}'.")


def decrypt_file(filename):
    if not os.path.exists(KEY_FILE):
        print(f"Error: Key file '{KEY_FILE}' not found. Cannot decrypt without the key.")
        return
    data = read_file(filename)
    if data is None:
        return
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()
    try:
        decrypted = Fernet(key).decrypt(data)
    except (InvalidToken, ValueError):
        print("Error: Decryption failed. Wrong key or not a file encrypted by this tool.")
        return
    folder, name = os.path.split(filename)
    if name.endswith(".enc"):
        name = name[:-4]
    output_name = os.path.join(folder, "decrypted_" + name)
    with open(output_name, "wb") as file:
        file.write(decrypted)
    print(f"Decrypted file saved as '{output_name}'.")


def main():
    print("File Encryption Tool")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Choose an option (1 or 2): ").strip()
    if choice not in ("1", "2"):
        print("Invalid option. Please choose 1 or 2.")
        return
    filename = input("Enter the filename: ").strip()
    if not filename:
        print("Filename cannot be empty.")
        return
    if choice == "1":
        encrypt_file(filename)
    else:
        decrypt_file(filename)


if __name__ == "__main__":
    main()