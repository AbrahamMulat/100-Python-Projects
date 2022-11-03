# --- coding: utf-8 ---
# @FileName  :swap_variable.py
# @Time      :11/3/2022 10:24 PM
# @Author    :Abraham
# @Software  :PyCharm

a = 3
b = 4

print(f"Before swap: a={a}, b={b}")

a, b = b, a  # same as a=b, b=a
print(f"After swap: a={a}, b={b}")

# Swap using a third variable
temp = a
a = b
b = temp
print(f"After swapping using a third variable: a={a}, b={b}")

# Swap two user input variables
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Before swapping: num1={num1}, num2={num2}")
num1, num2 = num2, num1
print(f"After swapping: num1={num1}, num2={num2}")