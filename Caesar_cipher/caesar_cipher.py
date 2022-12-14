# --- coding: utf-8 ---
# @FileName  :caesar_cipher.py
# @Time      :12/9/2022 8:38 PM
# @Author    :Abraham
# @Software  :PyCharm

"""
In cryptography, a Casesar cipher, also know as Caesar's cipher, the shift cipher, Caesar's code or
Caesar shift, is one of the simplest and most widely known encryption techniques. it is a type of
substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of
positions down the alphabet.
"""


def caesar_cipher(msg, shift_number):
    encrypted_msg = ""

    # transverse the plain txt
    for i in range(len(msg)):
        char = msg[i]
        # encrypt uppercase characters in plain txt
        if char.isupper():
            encrypted_msg += chr((ord(char) + shift_number - 64) % 26 + 65)
            # encrypt lowercase characters in plain txt
        else:
            encrypted_msg += chr((ord(char) + shift_number - 96) % 26 + 97)
    return encrypted_msg


# check the above function
msg = input("Enter your message: ")
shift_number = int(input("Enter the shift number: "))
print("Here is your encrypted message: " + caesar_cipher(msg, shift_number))


decrypted_msg = caesar_cipher(caesar_cipher(msg, shift_number), 26 - shift_number)
print(f"Here is your decrypted message: {decrypted_msg}")