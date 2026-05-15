#----------LOOP PRACTICE----------
'sum natural number'
# num_u = int(input('Enter a number: '))
# total_sum = 0
# for i in range(1, num_u + 1):
#     total_sum += i
# print(f'The sum of natural number from {1} to {num_u} is {total_sum}')
'even number'
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)
a = {1,2,3,4}
# b = {3,4,5,6}
#
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a.issubset(b))
# print(a.issuperset(b))
'reverse string' 'and' 'reverse words'
# text = 'I love python'
# # for i in range(len(text) - 1, -1, -1):
# #        print(text[i])
# # text_2 = input('Enter a string: ')
# # reversed_text = ''
# # for i in range(len(text_2)-1, -1, -1):
# #         reversed_text += text_2[i]
# # print(reversed_text)
#
# text = text.split()
# reversed_text = ''
# for i in range (len(text) - 1, -1, -1):
#     reversed_text += text[i] + ' '
# print(reversed_text.lstrip())
'count digit'
# numbers = 1234509805038870589765896756849
# count = 0
# for i in range(len(str(numbers))):
#     digit = numbers % 10
#     number = numbers // 10
#     count += 1
# print(count)
'is palindrome ?'
# while True:
#     print('-'* 12, 'Choice 1 or 2', '-' * 12)
#     print('1.Number')
#     print('2.String')
#     choice = int(input('Enter choice: '))
#     if choice == 1:
#         is_palindrome_n = int(input('Check number if it is a palindrome: '))
#         if str(is_palindrome_n)[0] == str(is_palindrome_n)[-1]:
#             print('Yes the number is a palindrome')
#         else:
#             print('Not a palindrome number')
#     elif choice == 2:
#         is_palindrome_s = input('Check string if it is a palindrome: ').lower()
#         if is_palindrome_s[0] == is_palindrome_s[-1]:
#             print('Yes the string is palindrome')
#         else:
#             print('Not a palindrome string')
#     else:
#         print('Invalid choice')
'is prime number'
# num = 99
# for n in range(2, 101):
#     is_prime = True
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             is_prime = False
#             break
# if is_prime:
#         print(f'{num} is a prime number')
# else:
#         print(f'{num} is not a prime number')
