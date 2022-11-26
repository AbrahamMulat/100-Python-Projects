# --- coding: utf-8 ---
# @FileName  :email_slicer.py
# @Time      :11/26/2022 9:20 PM
# @Author    :Abraham
# @Software  :PyCharm

email = "abcdefg1234@gmail.com"
print(email.strip())  # remove any whitespace or any unnecessary space
print(email.strip().partition("@"))  # split the email into username and domain name


def email_slicer(email):
    username, _, domain = email.strip().partition("@")
    return f"Your username is {username} & domain name is {domain}"


email = input("Enter Your Email: ")
print(email_slicer(email))
