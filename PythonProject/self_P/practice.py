# user_n = int(input('Enter your number: '))
# for n in range(1,user_n + 1):
#     if n % 3 == 0:
#         n = 'Fizz'
#     elif n % 5 == 0:
#         n = 'Buzz'
#     elif n % 3 == 0 and n % 5 == 0:
#         n = 'FizzBuzz'
#     print(n)
'sum, average,max,min'
from curses.ascii import isdigit
from operator import indexOf

# list_nums = [98, 30, 60 ,34, 24, 901]
#
# def analyze_numbers(n):
#     t_sum = 0
#     average = 0
#     maximum = list_nums[0]
#     minimum = list_nums[0]
#     for num in list_nums:
#         t_sum += num
#         if num > maximum:
#             maximum = num
#         if num < minimum:
#             minimum = num
#         average = round(t_sum / len(list_nums),2)
#     print(f'Total sum: {t_sum}')
#     print(f'Average: {average}')
#     print(f'Maximum: {maximum}')
#     print(f'Minimum: {minimum}')
#
# analyze_numbers(list_nums)
'count how many vowels'
# user_string = input("Enter a string ")
#
# vowels = ['a','e','i','o','u']
#
# vow = 0
# cons = 0
# for l in user_string:
#     if l.isalpha():
#         if l in vowels:
#             vow += 1
#         elif l not in vowels:
#             cons += 1
# # vow,cons = sum(l.isalpha() and l in vowels for l in user_string), sum(l.isalpha() and l in vowels for l in user_string)
# print(f'number of vowels: {vow}')
# print(f'number of consonants: {cons}')
'come'
# students = {
#     "Ali": 85,
#     "Sara": 92,
#     "John": 78,
#     "Liya": 88
# }
# total   = 0
#
# for key, value in students.items():
#     total += value
# average = total/len(students)
# print(f'Average: {average}')
# for key, value in students.items():
#     if value > average:
#         print(f'{key}: {value}')
# total   = 0
# count   = 0
# largest = 0
# while True:
#     user_input = int(input("Enter a number: "))
#     total += user_input
#     count += 1
#     if user_input > largest:
#         largest = user_input
#     if user_input == 0:
#         print(f'Total: {total}')
#         print(f'Count: {count - 1}')
#         print(f'Largest: {largest}')
#         break
'print unique number'
# nums = [3, 7, 2, 9, 4, 7, 2]
#
# new_list = []
# for n in nums:
#     if n not in new_list:
#         new_list.append(n)
# print(new_list)
'check strong password'
# def is_pwd_strong(pwd):
#     len_p = False
#     digit_n = False
#     upper_c = False
#
#     for l in pwd:
#         if l.isdigit():
#             digit_n = True
#         if l.isupper():
#             upper_c = True
#
#     if len(pwd) >= 8:
#         len_p = True
#
#     if all([len_p, digit_n, upper_c]):
#         print(True)
#     else:
#         print(False)
#
#
# pwd = input("Enter your password: ")
# is_pwd_strong(pwd)
'pwd generator'
# import random
# import string
#
# def strong_pwd(length):
#     if length < 4:
#         return 'Length must be at least 4!'
#     password = [
#         random.choice(string.ascii_lowercase),
#         random.choice(string.ascii_uppercase),
#         random.choice(string.digits),
#         random.choice(string.punctuation)
#     ]
#     all_chars = string.ascii_letters + string.digits + string.punctuation
#     for _ in range(length - 4):
#         password.append(random.choice(all_chars))
#     random.shuffle(password)
#     return "".join(password)
# print(strong_pwd(8))
'printing patter'
# row = ''
# for i in range(1,6):
#     i = str(i)
#     row += i
#     print(row)

data = [10, "20", 30, "40", "hello", 50]

# numerical_data = []
# total = 0
#
# for n in data:
#     if isinstance(n, int):
#         numerical_data.append(n)
#         total += n
#     elif isinstance(n, str) and n.isdigit():  # string that is numeric
#         n_int = int(n)                        # convert to integer
#         numerical_data.append(n_int)
#         total += n_int
#
# print(f"Total: {total}")
# print(f"Numerical data: {numerical_data}")
list_n = []
# while True:
#     print('1. Add number')
#     print('2. Remove number')
#     print('3. Show number')
#     print('4. Exit')
#     choice = int(input('Please input your choice: '))
#     if choice == 1:
#         while True:
#             add = int(input('Please input your number(0 to exit): '))
#             list_n.append(add)
#             if add == 0:
#                 break
#     elif choice == 2:
#         while True:
#             remove = int(input('Please input No you want to remove(0 to exit): '))
#             if remove == 0:
#                 break
#             if len(list_n) > 0 and remove in list_n:
#                 list_n.remove(remove)
#                 print(f'{remove} has been removed')
#             else:
#                 print('Please check the number if exited, Below press 0 then press 3 to check')
#     elif choice == 3:
#         if 0 in list_n:
#            list_n.remove(0)
#         print(list_n)
#     elif choice == 4:
#         print('Bye')
#         break
#     else:
#         print('Please inter valid choice')

li = 'hello world'
li_n = li.replace(li[2], 'L', 1)
print(li_n)
