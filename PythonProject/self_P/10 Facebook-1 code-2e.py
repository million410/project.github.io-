# Checking weather the number is Armstrong or not -------
from charset_normalizer.cd import alphabet_languages


# while True:
#     while True:
#         num = input("Enter a number: ")
#         # Is it natural number ----?
#         if num.isdigit():
#             num = int(num)
#             temp = num
#             if num > 0 and num.is_integer():
#                 break
#             else:
#                 print('Not natural number!')
#         else:
#             print('Possible only numbers')
#     sum_n = 0
#     while num > 0:
#         cube = num % 10
#         sum_n += cube ** 3
#         num = num // 10
#     if sum_n ==temp:
#         print(f'{temp} is Armstrong number')
#         break
#     else:
#         print('Not an Armstrong number')

# Question write a program to swap two variable.

#solution:

#--know total index ---

def is_correct_number(str_n, base):
    str_n = str(str_n).upper() # this is converting to upper case!
    if base < 2 or base > 36:
        print('base must be between 2 and 36')
        return False
    for char in str_n:
        if char.isdigit():
            val = int(char)
        elif char.isalpha():
            val = ord(char) - ord('A') + 10
        else:
            return False

        if val >= base:
            return False
    return True
print(is_correct_number('abc', 16))

# Ask again program -----

name = input('Enter your name: ')

while name == '':
    print("You didn't type anything!")
    name = input('Enter your name: ')
print(f"Your name is {name}")


try:
    age = int(input('Enter your age: '))
    while age <= 0:
        print('Your age must be greater than 0')
        age = int(input('Enter your age: '))
except Exception as e:
    print('You must type a number!')