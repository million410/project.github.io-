#Error Handling in python
try:
   print(1/0)
except:
    print('Error has been happened')




#-----Comprehension in python(Create Great One-Liners)------
toggle = True
word = 'Enable' if toggle else 'Disable'

print(word)
# ----List Comprehensions-
items = ['item_1', 'item_2', 'item_3', 'wrong_data']

upper_items = [item.upper() for item in items if 'item_' in item]
print(upper_items)

#✅ Exercise with list comprehensions

numbers = [1,2,3,4,5]
num_sq = [num ** 2 for num in numbers ]
num_cube = [num ** 3 for num in numbers if num % 2 == 0]
even_odd = ['Even' if num % 2 == 0 else 'Odd' for num in numbers]
print(num_sq)
print(num_cube)
print(even_odd)

mats = ['wood', 'steel', 'concrete', 'bricks', 'glass', 'plaster']
mats = [mat for mat in mats if 'o' in mat]
print(mats)

#dict comprehensions------
mats = ['wood', 'steel', 'concrete', 'bricks', 'glass', 'plaster']
dict_mats = {mat.upper():mat.lower() for mat in mats}
print(dict_mats)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
even_num = [num for li in matrix for num in li if num % 2 == 0 or num ==5]
print(even_num)

sentence = 'Python makes programming very powerful and fun'
spit_sen = {word:len(word) for word in sentence.split()}
print(spit_sen)

nums = [4, -3, 7, 0, -1, 8, 11]
# for num in nums:
#     if num % 2 == 0 and num >= 0:
#         print('Odd')
#     elif num % 2 != 0 and num >= 0:
#         print('Even')

even_odd = ['Even' if num % 2 == 0 and num > 0 else 'Odd' for num in nums]
print(even_odd)

text     = 'Education is powerful'
vowels = {ch.lower() for ch in text if ch.lower() in 'aeiou'}
print(vowels)

gen = (n*n for n in range(2,51) if all(n % i != 0 for i in range(2,int(n ** 0.5) + 1)))
for value in gen:
    print(value)

sentence   = 'programming education improves logical thinking'
word_vowel = {word:sum(1 for ch in word.lower() if ch in 'aeiou') for word in sentence.split() if sum(1 for ch in word.lower() if ch in 'aeiou') >= 2}
print(word_vowel)

nums = [10, 15, 20, 25, 30]
co = 0
even_tuples = [n for n in nums if n % 2 == 0]
print(even_tuples)

text   = 'Python is powerful'
condition = False
en_con = [letter for letter in text for vow in 'aeiou' if vow != letter and '' != letter]
print(en_con)