# --- coding: utf-8 ---
# @FileName  :palindrome.py
# @Time      :11/9/2022 11:26 PM
# @Author    :Abraham
# @Software  :PyCharm


# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards,
# such as the words madam or racecar

def is_palindrome(word):
    if word == word[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
    return word


word = input("Enter a word: ")
num = "121"
is_palindrome(word)
is_palindrome(num)

