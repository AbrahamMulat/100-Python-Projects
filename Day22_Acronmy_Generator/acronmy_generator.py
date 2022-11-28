# --- coding: utf-8 ---
# @FileName  :acronmy_generator.py
# @Time      :11/28/2022 11:52 PM
# @Author    :Abraham
# @Software  :PyCharm

user_input = input("Enter a phrase or sentence: ")
phrase = user_input.replace("of", "").split()
acronmy = ""
for word in phrase:
    acronmy += word[0].upper()

print(f"The acronym of {user_input} is: {acronmy}")