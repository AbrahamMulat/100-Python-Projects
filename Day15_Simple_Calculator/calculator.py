# --- coding: utf-8 ---
# @FileName  :calculator.py
# @Time      :11/17/2022 9:30 PM
# @Author    :Abraham
# @Software  :PyCharm

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def square(x):
    return x * x


def square_root(x):
    return pow(x, 0.5)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice... "))
    if choice == 1:
        print("The computed addition result is : ", add(num1, num2))
    elif choice == 2:
        print("The computed subtraction result is : ", subtract(num1, num2))
    elif choice == 3:
        print("The computed product result is : ", multiply(num1, num2))
    elif choice == 4:
        print("The computed division result is : ", round(divide(num1, num2)))
    elif choice == 0:
        print("Exit")
    else:
        print("Sorry, invalid choice!")
print()
