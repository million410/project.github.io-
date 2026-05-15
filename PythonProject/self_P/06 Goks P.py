
# def fizz_buzz():
#     while True:
#         num1 = input('Inter the starting point: ')
#         num2 = input('Inter the ending point: ')
#         if num1.isdigit() and num2.isdigit():
#             num1 = int(num1)
#             num2 = int(num2)
#             for i in range(num1, num2 + 1):
#                 if i % 3 == 0 and i % 5 == 0:
#                     print('FizzBuzz')
#                 elif i % 3 == 0:
#                     print('Fizz')
#                 elif i % 5 == 0:
#                     print('Buzz')
#                 else:
#                     print(i)
#             break
#         else:
#             print('Please enter a number for both.')
#
# fizz_buzz()
'Count vowels'
# def count_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     # Use sum to count 1 for every character in input_string found in vowels
#     return sum(1 for char in input_string if char in vowels)
#
# # Example usage:
# result = count_vowels("Addis Ababa")
# print(result)  # Output: 6
'second largest number'
# numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# def kth_largest(number, k):
#     nums = number.copy()
#     for _ in range(k):
#         max_n = max(nums)
#         nums.remove(max_n)
#     return max_n
#
# print(kth_largest(numbers, 2))  # 2nd largest
'Simple calculator'
# print('Print two numbers and perform all arithmetic operations on them.')
# while True:
#     try:
#         num1 = input('Please enter the first number: ')
#         num2 = input('And the second number: ')
#         if num1.isdigit() and num2.isdigit():
#             num1 = int(num1)
#             num2 = int(num2)
#             add = num1 + num2
#             sub = num1 - num2
#             mul = num1 * num2
#             div = num1/num2
#             print('The sum is:- - - - - - ', add)
#             print('The difference is(f-s):', sub)
#             print('The multiplication is:-', mul)
#             print('The division is:- - - -', div)
#             break
#         else:
#             print('Please enter a natural number')
#     except Exception as e:
#         print(f"{type(e).__name__}: Happened")
'Anagrams'
# word = 'tea'
# word2 = 'eat'
# check, check2 = False, True
# for l in word2.lower():
#     if l in word.lower():
#         check = True
#     else:
#         check2 = False
# condition = [check, check2]
# if all(condition):
#     print(True)
# else:
#     print(False)
# word1 = 'tea'
# word2 = 'eat '
# print(sorted(word1.lower().replace(' ', '')) == sorted(word2.lower().replace(' ', '')))
'Find longest word'
# import random
# sentence = "The quick brown fox jumps over the lazy dog."
# separated_sentence = sentence.split(' ')
# dict_form = {word: len(word) for word in separated_sentence}
# longest = max(dict_form.values())
# the_word = [k for k, v in dict_form.items() if v == longest]
# print(f'Longest word in the sentence: {random.choice(the_word)}')

import random
import string

# sentence = "The quick brown fox jumps over the lazy dog."
#
# words = sentence.translate(str.maketrans('', '', string.punctuation)).split()
#
# longest = max(len(word) for word in words)
#
# candidates = [word for word in words if len(word) == longest]
#
# print(f"Longest word in the sentence: {random.choice(candidates)}")
import math
'Palindrome Number Checker'
# while True:
#     num = input('Try to inter Palindrome num: ')
#     if num.isdigit():
#         num = int(num)
#         num_digits = int(math.log10(num)) + 1
#         if num // (10 ** (num_digits - 1)) == num % 10:
#             print('Palindrome')
#             print('Good Job!')
#             break
#         else:
#             print('Not Palindrome')
#     else:
#         print('please enter a number')
'group anagrams'
#
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# # Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
#
# groups = {}
#
# for word in words:
#     key = ''.join(sorted(word))
#     print(key)
#     groups.setdefault(key, []).append(word)
#
# output = list(groups.values())
#
# print(output)
#
# numbers = [1,2,4,5,7,8,9]
# missing_num = []
# for i in range(numbers[0], numbers[-1]+1):
#       if i not in numbers:
#         missing_num.append(i) #Append the missing number to the list----
# print(f'Missing number is: {missing_num}')
#
# nums = [19, 12, 13, 4,15]
# arranged = sorted(set(nums), reverse=True)
# print(arranged[1])
'Filtering a number'
# for i in range(2000, 3200):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i)
'sum or product'
# a = 35
# b = 67
# result = a * b if a * b > 1000 else a + b
# print('Result:', result)
'Palindrome string'
# word_1 = 'Simples'
# result = 'Palindrome' if word_1.lower()[0] == word_1.lower()[-1] else 'Not Palindrome'
# print(result)
'frequency of char'
# word = 'This text check the frequency of char'
# text_only = word.replace(' ', '')
# fre = {}
# for l in text_only.lower():
#     count_l = text_only.count(l)
#     fre[l] = count_l
# for k, v in fre.items():
#     print(f'{k} --> {v} times')
up_to = 12
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144//// c = 0, a = 1
for i in range(up_to + 1):
    c = i
    a = i + 1
    b = c
dict_l = {
    'Alex': 12,
    'Eyob': 67,
    'John': 54
}
for k, v in dict_l.items():
    if v == 54:
        print(v, '---->', k)