# --- coding: utf-8 ---
# @FileName  :max_of_n_number.py
# @Time      :11/4/2022 9:41 PM
# @Author    :Abraham
# @Software  :PyCharm

# 1. Find max of n numbers using built-in max() function
# max_num = 0
# num_list = []
# n = int(input("How many numbers: "))
# for i in range(n):
#     nums = int(input(f"Enter number {i + 1}: "))
#     num_list.append(nums)
# print(max(num_list))


# 2. Find the maximum of n numbers using user-defined function
def find_max(n):
    max_num = 0
    num_list = []
    for i in range(n):
        nums = int(input(f"Enter number {i + 1}: "))
        num_list.append(nums)
        if num_list[i] > max_num:
            max_num = num_list[i]
    return f"The maximum number is {max_num}"


print(find_max(5))
