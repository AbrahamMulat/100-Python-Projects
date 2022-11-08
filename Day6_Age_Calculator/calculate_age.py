# --- coding: utf-8 ---
# @FileName  :calculate_age.py
# @Time      :11/8/2022 9:03 PM
# @Author    :Abraham
# @Software  :PyCharm

import datetime


def calculate_age(birth_year, birth_month, birth_day):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year

    return print(f"You are {age} years and {birth_month} months and {birth_day} days")


birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

calculate_age(birth_year, birth_month, birth_day)
