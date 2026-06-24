from cryptography.fernet import Fernet
from tkinter import messagebox, simpledialog, Tk
import pyperclip

encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def encrypt_with_cryptography(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_with_cryptography(encrypted_message):
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

def copy_to_clipboard(message):
    pyperclip.copy(message)
    messagebox.showinfo('Success', 'Message copied to clipboard!')

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

root = Tk()

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        swapped = swap_letters(message)
        encrypted = encrypt_with_cryptography(swapped)
        messagebox.showinfo('Ciphertext of the secret message is: ', encrypted)
        copy_choice = messagebox.askyesno('Copy?', 'Do you want to copy this to clipboard?')
        if copy_choice:
            copy_to_clipboard(encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted_crypto = decrypt_with_cryptography(message)
        decrypted = swap_letters(decrypted_crypto)
        messagebox.showinfo('Plaintext of the secret message is: ', decrypted)
    else:
        break
    root.mainloop

