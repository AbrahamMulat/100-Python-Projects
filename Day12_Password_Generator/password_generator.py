# --- coding: utf-8 ---
# @FileName  :password_generator.py
# @Time      :11/14/2022 11:58 PM
# @Author    :Abraham
# @Software  :PyCharm

import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation

alphabet = letters + digits + special_characters

password_length = int(input("Enter the length of your password: "))

# genrate a password string
password = ""
for i in range(password_length):
    password += secrets.choice(alphabet)

print(password)

# generate a user-input password length password with at least one lowercase characters, at least one uppercase
# characters, at least one special character and at least three digits.
while True:
    password_1 = ''.join(secrets.choice(alphabet) for i in range(password_length))
    if (any(c.islower() for c in password_1)
            and any(c.isupper() for c in password_1)
            and any(c in special_characters for c in password_1)
            and sum(c.isdigit() for c in password_1) >= 3):
        break
print(password_1)
