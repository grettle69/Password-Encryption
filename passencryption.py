from cryptography.fernet import Fernet
import getpass

# Encrypt a password using the key
def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Decrypt a password using the key
def decrypt_password(key, encrypted_password):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password)
    return decrypted_password.decode()

# Save the encrypted password to a file
def save_encrypted_password(application, encrypted_password):
    with open('encryption-data.txt', 'a') as file:
        file.write(f'Application: {application}\n')
        file.write(f'Encrypted Password: {encrypted_password.decode()}\n\n')

# Main function
def main():
    # Generate a new encryption key
    key = Fernet.generate_key()
    print("Your encryption key is:", key.decode())

    # Get the application name from the user
    application = input("Enter application name: ")

    # Get the password from the user
    password = getpass.getpass("Enter password: ")

    # Encrypt the password
    encrypted_password = encrypt_password(key, password)
    print("Encrypted password:", encrypted_password)

    # Decrypt the password
    decrypted_password = decrypt_password(key, encrypted_password)
    print("Decrypted password:", decrypted_password)

    # Save the encrypted password and application name to a file
    save_encrypted_password(application, encrypted_password)

if __name__ == "__main__":
    main()
