# from os.path import join
#
# x = 5.2345
# x = int(x)
#
# y = 6
# y = complex(x, y)
# print(y)
#
# price = 9
# print(f'The price is {price:.2f} Dollars')
#
# age = 36
# txt = f"My name is John, and I am {age}"
# print(txt)
#
# a = 'k'
# b = 'l'

#     1
#    222
#   33333
#  4444444
# 555555555
#66666666666

"tree pattern"
# row = 20
# for i in range(1, row + 1):
#     num_str = '*' * (2 * i - 1)
#     space = ' ' * (row - i)
#     comb = space + num_str
#     print(comb)
# n = 5
# for i in range(n):
#     for j in range(n):
#         print('*', end=' ')
#     print()
# *****
# ****
# ***
# **
# *
# *
# **
# ***
# ****
# *****
n = 5
# def form_tri(n):
#     for i in range(n, 0, -1):
#         print('*' * i)
# def num_t(n):
#     for i in range(1, n + 1):
#         print('*' * i)
#
# for i in range(1, 11):
#     num_t(5)
#     form_tri(5)
'alpha loop'
# A
# A B
# A B C
# A B C D

# letters = ['A', 'B', 'C', 'D']
#
# for i in range(1, len(letters) + 1):
#     for j in range(i):
#         print(letters[j], end=' ')
#     print()
'alpha'
# while True:
#     ph_value = input('Insert the pH value of the solution: ')
#     if ph_value.isdigit():
#         ph_value = int(ph_value)
#         match ph_value:
#             case 60:
#                 print('You close the system')
#                 break
#             case n if n < 7 and n > -1:
#                 print('The solution is Acidic')
#             case n if n > 7 and n < 15:
#                 print('The solution is Basic')
#             case n if n == 7:
#                 print('The solution is Neutral')
#             case _:
#                 print('The pH value is always between -1 and 15 natural number')
#     else:
#         print('Allowed only Numbers!')
'error 1'
# try:
#     number = int(input("Enter a number: "))
#     result =  100/number
#     print(result)
# except ValueError:
#     print('Error: Please enter a valid integer.')
# except ZeroDivisionError:
#     print('You can not divide by zero.')
#
# print(sum)
'error 2'
# def set_temperature(temp):
#     if temp < -273.15:
#         # Manually triggering a built-in error
#         raise ValueError("Temperature below absolute zero is impossible!")
#     return f"Temperature set to {temp}°C"
#
# try:
#     print(set_temperature(-300))
# except ValueError as e:
#     print(f"Validation Error: {e}")
'safe number input'
# try:
#     user_n = int(input('Write a number you want to square: '))
# except Exception as e:
#     print(f'Invalid({type(e).__name__}): try again!')
# else:
#     print(user_n * user_n)
# finally:
#     print('Program finished!')
'division program'
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print('Cannot divide by zero')
# else:
#     print(a/b)
# finally:
#     print("Program Ended!")
'File reader'
# def access_file(filename):
#     with open(filename, 'r') as file:
#         content = file.read()
#         for n, line in enumerate(content):
#             if n == 3:
#                 continue
#         return line
# try:
#     access_file('notes.txt')
# except FileNotFoundError:
#     print('File not found')
# else:
#     access_file('notes.txt')
# finally:
#     print('Closing operation complete')

# filename = 'server.log'
'🧠 1. Smart Log Analyzer (Files + Dict + Exceptions)'
# try:
#     with open(filename, 'r') as f:
#         counts = {
#             'INFO': 0,
#             'ERROR': 0,
#             'WARNING': 0
#         }
#
#         for line in f:
#             if 'INFO' in line:
#                 counts['INFO'] += 1
#             elif 'ERROR' in line:
#                 counts['ERROR'] += 1
#             elif 'WARNING' in line:
#                 counts['WARNING'] += 1
#
#     # Print results
#     for key, value in counts.items():
#         print(f"{key} -> {value}")
#
#     # Find most frequent
#     most_frequent = max(counts, key=counts.get)
#     print("Most frequent:", most_frequent)
#
# except FileNotFoundError:
#     print("File not found")
'🧠 2. Student Score Manager (Functions + Lists + Sorting'

students = [
    ("Million", 78),
    ("Ebba", 95),
    ("Ephrem", 60),
    ("Monera", 88)
]
def student_score_manager(students):
    pass


def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    # Use sum to count 1 for every character in input_string found in vowels
    return sum(1 for char in input_string if char in vowels)

# Example usage:
result = count_vowels("Addis Ababa")
print(result)  # Output: 6