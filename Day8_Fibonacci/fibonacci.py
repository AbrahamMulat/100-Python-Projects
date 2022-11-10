# --- coding: utf-8 ---
# @FileName  :fibonacci.py
# @Time      :11/10/2022 7:29 PM
# @Author    :Abraham
# @Software  :PyCharm

"""In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, the Fibonacci sequence, in which each
number is the sum of the two preceding ones. The sequence commonly starts from 0 and 1, although some authors start
the sequence from 1 and 1 or sometimes (as did Fibonacci) from 1 and 2. Starting from 0 and 1, the first few values
in the sequence are:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144. --wikipedia
The Fibonacci numbers may be defined by the recurrence relation
F0 = 0, F1 = 1
and
Fn = Fn-1 + Fn-2  for n>1.

"""


# The following program finds the fibonacci of a number n and prints all the fibonacci sequence up to that number.

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(20):
    print(fibonacci(i))
