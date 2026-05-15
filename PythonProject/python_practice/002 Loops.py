# # GUESS A NUMBER
#
# import random
#
# # RULES
# min        = 1
# max        = 20
# secret_num = random.randint(min, max)
# # Ask user for Input
# attempts = 1
# for i in range(5):
#     attempts += 1
#     guess = input(f'❓ Guess the secret number between {min} and {max}: ')
#     guess = int(guess)
#
#
#     print('-'*50, f'Attempt {i + 1}/5')
#     # check the input
#     if guess < min or guess > max:
#         print(f'⛔Incorrect Input. Guess a number between {min} and {max}.')
#     # Check result
#     elif guess == secret_num:
#         print('🎃Correct! You guessed it.')
#         break
#     elif guess > secret_num:
#         print('❌ Too high! Try again.')
#     else:
#         print('❌ Too low! Try again.')

# Ready to learn about loops?
#
# container = [1, 2, 3, 4, 5]
#
# for num in container:
#     print(num)
#     print(num)
#     print(num)



#--------Loop Over List

# List_material = ['Wood', 'Steel', 'Glass', 'Bricks']
# print('hellow'.upper())
# for mat in List_material:
#     print(mat)
#     print(mat.lower(), mat.upper())


# Loop Over String----------------------------
#
# text = 'Hello python Hackers'
#
# for char in text:
#     lower_char = char.lower()
#     upper_Char = char.upper()
#     print(lower_char, '----' , upper_Char)


# Loop Over Digits-------------

# big_number = 123456789
#
# for str_num in str(big_number):
#     num = int(str_num)
#     sq  = num**2
#     cube = num**3
#     print(num, sq, cube)

# for i in range(1, 201, 20):
#     print(i)
#
#
# # for i in range(50):
#     print('Hello')
# floor_plans = []
# for i in range(1,11):
#     plan_name = f'Foorplan_{i}'
#     floor_plans.append(plan_name)
#
# print(floor_plans)

# floor_plans.remove('Foorplan_3')
# print(floor_plans)
# floor_plans.pop()
# print(floor_plans)
# floor_plans.reverse()
# print(floor_plans)
# floor_plans.extend(['a','b','c'])
# print(floor_plans)
# floor_plans.sort()
# print(floor_plans)
nums  = [1, 99, 23, 40, 57, 6, 81]

# for n in nums:
#     if n % 2 == 0 and n != 0:
#         print(f'First even number is: {n}')
#         break
# print('Finished')
#
# # Continue iteration-----------------
# real_money = [5, 10, 20, 50, 100, 500]
# wallet     = [5, 20, 10, 50, 25]
#
# total = 0
#
# for note in wallet:
#     if note not in real_money:
#         continue
#     total += note
# print(f'Total: {total} EUR')

# Nested Loops-----------------
'hellow'
# course = [
#     ['Lesson_01.01', 'Lesson_01_02', 'Lesson_01_03', 'Lesson_01_04'],
#     ['Lesson_02.01', 'Lesson_02_02', 'Lesson_02_03'],
#     ['Lesson_03.01', 'Lesson_03_02']
# ]
# for module in course:
#     print(f'Starting Module: {module}')
#     for lesson in module:
#         print(f'Completed: {lesson}')
#     print('Module is completed')
#     print('------')
'heel'
# for x in range(1,11):
#     for y in range(1,11):
#         for z in range(1,11):
#           print(x,y, z)

# While Loop
#-------------------------------------------
# Iterable Objects

list_nums  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_items = ['a', 'b', 'c', 'd']
tuple_nums = (1, 2, 3, 4, 5)
string     = 'Text is sequence of characters'
range_10   = range(100)
dict_items = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


# count = 0
# while count < 100:
#     print('Attemp:', count)
#     count += 1

# 9 Ticketing Machine Example
#-----------------------------

tickets   = 100

# while True:
#     n = input('Buy Tickets: ')
#     n = int(n)
#
#     # Sell Ticket
#     if n < 0:
#         print('Please, Insert Valid Number')
#         continue
#     elif n < tickets:
#       tickets -= n
#       print(f'Tickets Left: {tickets}')
#     elif n > tickets:
#       print(f'Sorry, we have only {tickets} tickets left')
#     elif n == tickets:
#         print('Sold Out!')
#         break

'Fibonacci Number'
# a  = 0
# b  = 1
#
# number_names = [
#     '',
#     'thousand',
#     'million',
#     'billion',
#     'trillion',
#     'quadrillion',
#     'quintillion',
#     'sextillion',
#     'septillion',
#     'octillion',
#     'nonillion',
#     'decillion',
#     'bajillion',
#     'quintillion',
#     'sextillion',
#     'septillion',
#     'octillion',
# ]
#
# for i in range(175):
#     num          = f'{a: ,d}'
#     count_commas = num.count(',')
#     large_num    = number_names[count_commas]
#     print(large_num, num)
#     c = a + b
#     a = b
#     b = c

'for loop'
# for i in range(1,20):
#     if i % 2 != 0:
#         continue
#     print(i)
'print triangular star'
# for i in range(1,6):
#     how   = '*'*i
#     count = how.count('*')
#     hy    = '-'*(5-count)
#     print(count, how, hy)
# sum = 0
# while True:
#     sum += sum
#     sum += 1
#     if sum > 100:
#         break
# print(sum)
#
# a = 0
# b = 1
# first = 0
# while True:
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     first += 1
#     if first == 7:
#         break
import random
# min_num = 1
# max_num = 50
# secret_num = random.randint(min_num, max_num)
# count = 0
# attempt = 0
# while True:
#     user_input = input(f'Guess a number between {min_num} and {max_num}: ')
#     user_input = int(user_input)
#     attempt += 1
#     print(f'❌Wrong!, Try again!{'-'*20}{5-attempt} attempts left')
#     if user_input == secret_num:
#         print(f'You got it!, in {attempt} attempts')
#         break
#     if attempt == 5:
#         print('Game Over')
#         pl_again = input('Are you ready to play again?: ')
#         if pl_again not in ['yes', 'ok', 'i want', 'yah!']:
#             break
#         continue
go = 3456
# go = str(go)
# print(len(go))
# co = int(go[1]) + int(go[0])
# print(co)
# for i in range(100,1000):
#     str_n = str(i)
#     for s in range(0,len(str_n)):
#         yu = int(str_n[s])
#         s += 1
#         yu += int(str_n[s])
#     print(yu)

# for num in range(1, 100):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=' ')

for num in range(100,1000):
    string = str(num)
    list_str = list(string)
    list_nums = [int(i) for i in list_str]
    sum_num = 0
    mul_num = 1
    for n in range(len(list_nums)):
        sum_num += list_nums[n]
        mul_num *= list_nums[n]
    if sum_num != mul_num:
        continue
    else:
        print(num)








