
# sum_n = 0
# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#        total += 1
# print('sum of even numbers is:', total)
#
# user_input = int(input('Enter a number: '))
# c = 1
# for i in range(1, user_input + 1):
#      c = c * I
# print(f'factorial of {user_input} is {c}')
#
# number = int(input('Enter a number: '))
# reverse = 0
# real = number
# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number = number // 10
# print(f'Reverse of {real} is {reverse}')

num_i = 2765
count = 0
while num_i > 0:
    count += 1
    num_i //= 10

# is prime number
n  = 12
is_prime = True
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
if is_prime:
    print('yes prime!')
else:
    print('not prime!')

m = 10
a = 0
b = 1
fab_n = []
# while a < 15:
#     fab_n.append(a)
#     a, b = b, a + b
# print(fab_n)
#
# for i in range(1,10):
#     print(i, 'x' * i)
#
# tes = [1,2,3,4,5,6]
# print(len(tes))
#
# fil_n = [18,45,53,8,12,0,34,79,4,109,1,2,1,453,267,900,23,50]
#
# for i in range(1, len(fil_n)):
#     a, b = fil_n[i-1], fil_n[i]
#     if a < b:
#         a = b
#
# print(a)
# sum_up = 0
# while True:
#     user = int(input('Enter a number: '))
#     sum_up += user
#     if user == 0:
#         print('Total entered number is:', sum_up)
#         break
# even = 0
# odd = 0
# for i in range(1,11):
#     user = int(input('Enter a number: '))
#     if user % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
#     if i == 10:
#         print('Even number:', even)
#         print('Odd number:', odd)

correct_pass = '14ASV89i'

# while True:
#     user = input('Inter the password:')
#     if user == correct_pass:
#         print('correct!')
#         break
balance = 1000
# while True:
#     print('\n---ATM MENU----')
#     print('1.Check balance')
#     print('2.Withdraw')
#     print('3.Deposit')
#     print('4.Exit')
#     choice = int(input('Enter your choice:'))
#     if choice == 1:
#         print('Your balance:', balance)
#     elif choice == 2:
#         amount = int(input('Enter amount:'))
#         if amount < balance:
#             balance -= amount
#             print('Please take your cash')
#             print('New balance:', balance)
#         else:
#             print('Your balance is insufficient')
#     elif choice == 3:
#         amount = int(input('Enter amount:'))
#         balance += amount
#         print('Your new balance:', balance)
#     elif choice == 4:
#         break
#     else:
#         print('Please enter a valid choice')
total = 0
# count = 0
# print('\n--subject order')
# print('1.English')
# print('2.Maths')
# print('3.Chemistry')
# print('4.Biology')
# print('5.physics')
# while count <= 5:
#     count += 1
#     mark = int(input(f'Enter your Mark({count}): '))
#     total = total + mark
#     if count == 5:
#         print('Your Average Mark is', total/count)
#         break
stop = 0
# while stop < 6:
#     stop += 1
#     ch = str(stop)
#     print(f'{ch * stop}')
'hello'
# num = int(input('Enter a number: '))
# original = num
# sum_fact = 0
# while num > 0:
#     digit = num % 10
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
#     sum_fact += fact
#     num //= 10
# if sum_fact == original:
#      print('strong Number')
# else:
#      print('not strong Number')
# use = 8
# prod = 1
# for i in range(0, use):
#     b = use - i
#     prod *= b
#     if b == 1:
#         break
# print(prod)
empty = []
# for t in range(1, 6):
#     table = f'Table {t}'
#     for i in range(1, 11):
#         prod = t * i
#         tab_form = f'{prod}'
#         empty.append(tab_form)
#         if i == 10:
#
#             print(table, (empty))
#             empty = []
name = 'Million'
# password = '1234567'
# attempt = 0
# while True:
#     attempt += 1
#     if attempt > 3:
#         print('Too many attempts!, Account Locked')
#         break
#     us_name = input('Enter your name: ')
#     us_password = input('Enter your password: ')
#     if us_name == name and us_password == password:
#         print('Login Successful!')
#         break
#     else:
#         print('Try again! 📛')

# sum_m = 0
# while True:
#     digit = n % 10
#     sum_m += digit
#     n //= 10
#     if n == 0:
#         print(sum_m)
#         if sum_m % 9 == 0 and sum_m % 3 == 0:
#             print('It also Divisible by 9 and 3')
#             break
#         else:
#             print('Not divisible by 3 and 9')
#             break
'is armstrong number???'
# is_armstrong_n = int(input('Identify Number (Armstrong or not?: '))
# original = is_armstrong_n
# sum_d = 0
# cube = 1
# while is_armstrong_n > 0:
#     digit = is_armstrong_n % 10
#     for i in range(1,4):
#         cube *= digit
#         if i == 3:
#             sum_d += cube
#             cube = 1
#             is_armstrong_n = is_armstrong_n // 10
# if int(sum_d) == original:
#     print('yes armstrong')
# else:
#     print('not armstrong')
# print(sum_d)
'single digit result'
# u_num = 987
# while u_num > 10:
#     total_n = 0
#     while u_num > 0:
#         digit = u_num % 10
#         total_n += digit
#         u_num //= 10
#     u_num = total_n
# print(total_n)
'are the same start and end'
# number = int(input('please a number that have the same start and end number: '))
# number = list(str(number))
# if number[0] == number[-1]:
#    print('yes')
# else:
#    print('no')
'how many vowel letter'
# vowels = ['a', 'e', 'i', 'o', 'u']
# str_s = 'hello world uganda'
# count = 0
# set_n = set()
# for char in str_s:
#     if char in vowels:
#         set_n.add(char)
# print(f'There are {len(set_n)} unique vowels in this string{list(set_n)}')
'power with loop'
# base = 3
# power = 4
# result = 1
# for i in range(1, power + 1):
#     result *= base
# print(result)
'find smallest number'
# li_n = [345,675,58,201,22,100,99]
# b = li_n[0]
# for num in li_n:
#     if num < b:
#         b = num
# print(f'smallest number is {b}')
'is perfect number'
# num = 6
# sum_n = 0
# for i in range(1,num):
#     if num % i == 0:
#         sum_n += i
# if sum_n == num:
#     print('the number is perfect')
# else:
#     print('the number is not perfect')
'pyramid patter'
# n = 4
# for row in range(1, n + 1):
#     for s in range(n - row):
#         print(' ', end='')
#     for star in range(2 * row - 1):
#         print('*', end='')
#     print()
'remove digits'
# num = 12232
# remove = 2
#
# result = 0
# place = 1
# while num > 0:
#     digit = num % 10
#     if digit != remove:
#         result = digit * place + result
#         place *= 10
#     num //= 10
# print(result)
row = 4
#
# for i in range(1, row + 1):
#     print(' ' *  (row - i),'x' * (i * 2 - 1))
# num_1 = int(input('First number: '))
# num_2 = int(input('Second number: '))
# least = 0
# for i in range((num_1 * num_2 + 1), 1, -1):
#     if i % num_2 == 0 and i % num_1 == 0:
#         least = i
# print(least)
'Number to binary code'
# digital_n = 65
# binary_n = bin(digital_n)
# binary_n = binary_n[2:]
# print(binary_n)
'binary number to decimal number'
# binary_n = 1001
# sum_b = 0
# count = -1
# while binary_n > 0:
#     bin = binary_n % 10
#     binary_n = binary_n // 10
#     count += 1
#     sum_b += (2 ** count) * bin
# print(sum_b)
'decimal number to binary number'
# decimal_n = 13
# binary = ''
# while decimal_n > 0:
#     remainder = decimal_n % 2
#     binary += str(remainder)
#     decimal_n //= 2
# print('Binary: ',binary)
''
# num = int(input('Enter a number: '))
# freq = [0] * 10
# print(freq)
# while num > 0:
#     digit = num % 10
#     freq[digit] += 1
#     num //= 10
# for i in range(10):
#     if freq[i] > 0:
#         print(i, '->', freq[i], 'time(s)')
'Menu Drive calculator'
# while True:
#     print(1 ,'->', 'Add')
#     print(2 ,'->', 'Subtract')
#     print(3 ,'->', 'Multiply')
#     print(4 ,'->', 'Divide')
#     print(5 ,'->', 'Exist')
#     user_choice = int(input('choice operation: '))
#     if user_choice == 1:
#         user_1 = int(input('Enter a number: '))
#         user_2 = int(input('Enter another number: '))
#         print('Result: ',user_1 + user_2)
#     elif user_choice == 2:
#         user_1 = int(input('Enter a number: '))
#         user_2 = int(input('Enter another number: '))
#         print('Difference: ',user_1 - user_2)
#     elif user_choice == 3:
#         user_1 = int(input('Enter a number: '))
#         user_2 = int(input('Enter another number: '))
#         print('Product: ',user_1 * user_2)
#     elif user_choice == 4:
#         user_1 = int(input('Enter a number: '))
#         user_2 = int(input('Enter another number: '))
#         print('Qoutient',user_1 / user_2)
#     elif user_choice == 5:
#         print('Stopped')
#         break
#     else:
#         print('Invalid input')
