# --- coding: utf-8 ---
# @FileName  :find_factorial.py
# @Time      :11/5/2022 8:38 PM
# @Author    :Abraham
# @Software  :PyCharm

def factorial(n):
    fact = 1
    if n < 0:
        return "The factorial of a negative number is undefined!!"
    elif n == 0:
        return f"The factorial of {n} is 0"
    for i in range(1, n + 1):
        fact = fact * i
    return f"The factorial of {n} is {fact}"


# print(factorial(1))


# find factorial of a number using recursive function
def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


print(fact(5))
