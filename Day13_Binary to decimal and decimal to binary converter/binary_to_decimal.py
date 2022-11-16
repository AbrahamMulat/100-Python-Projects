

def decimal_to_binary(num):
    is_quotient_one = False
    r_list = []
    while not is_quotient_one:
        q = num // 2
        if num == 0:
            r = 0
            r_list.append(r)
            break
        r = num % 2
        num = q
        if q == 0:
            r = 1
            is_quotient_one = True
        # print(r)
        r_list.append(r)
        # print(num)
    # print(r_list)
    result = int("".join([str(i) for i in r_list[::-1]]))
    return result


# for i in range(101):
#     print(i, decimal_to_binary(i))


def bin2decimal(binary_num):
    decimal = 0
    for digit in binary_num:
        decimal = decimal * 2 + int(digit)
    return decimal


bin_num = input("Enter a binary number: ")
print(bin2decimal(bin_num))
