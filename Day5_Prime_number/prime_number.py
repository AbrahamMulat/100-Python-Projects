# --- coding: utf-8 ---
# @FileName  :prime_number.py
# @Time      :11/7/2022 8:26 PM
# @Author    :Abraham
# @Software  :PyCharm

# python program to find all prime numbers in an interval a, b
def prime(n):
    primes = []
    for number in range(1, n + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                primes.append(number)

    return primes


print(prime(100))
