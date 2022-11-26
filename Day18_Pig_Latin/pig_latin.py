# --- coding: utf-8 ---
# @FileName  :pig_latin.py
# @Time      :11/26/2022 4:13 PM
# @Author    :Abraham
# @Software  :PyCharm


def pig_latin(en_word):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    vowel_index = 0
    # For words that begin with vowel sounds, one just adds ”hay”, "way" or "yay" to the end (or just "ay").
    if en_word[0] in vowels:
        return en_word + "ay"
    # For words that begin with consonant sounds, all letters before the initial vowels are placed at the end of the
    # word sequence. Then, "ay" is added
    elif en_word[0] not in vowels and en_word[1] in vowels:
        return en_word[1::] + en_word[0] + "ay"
    # When words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to
    # the end and then "ay" is added at last.
    else:
        for i in range(len(en_word)):
            if en_word[i] in vowels:
                vowel_index = i
                break
        return en_word[vowel_index:] + en_word[0:vowel_index] + "ay"


word = input("Enter any word: ")
print(pig_latin(word))

sentence = "Python is Awesome"
pig_latin_word = ""
for word in sentence.split():
    pig_latin_word += " " + pig_latin(word)
print(pig_latin_word)
