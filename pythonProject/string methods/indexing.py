# indexing = accesing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_number = "1234-5678-9012-3456"
# print(credit_number[6])

# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1]) -1, -2 ... returns in reverse order
# print(credit_number[:]) using just : python sees it as beggining or end depending on how many there are
# print(credit_number[::2]) counts every third character

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

reverse_numbers = credit_number[::-1]
print(reverse_numbers)