# print('hello world')
#
# # str_num_a = input('Insert First Number: ')
# # str_num_b = input('Insert Second Number: ')
# #
# # num_a = float(str_num_a)
# # num_b = float(str_num_b)
# #
# # total = num_a + num_b
# # print(total)
#
# # tuples data type
#
# empty_tuple = ()
#
# list_data = [1,2,3,4,5,6]
#
# data = (10, 20, 30, 40, 50, 60,56,20,10,40,20)
#
# data_pts = ((0,0,0),(1,2,3),(2,3,4))
#
#
# print(data[0])
# print(data[2])
# print(data[4])
# print(data_pts[1])
#
# print(data.count(20))
# print(data.index(20))
#
# print(data[2:])
# print(data[:2])
# print(data[1:3])
#
# # Set data type
#
# empty_set = set()
#
# set_item = {10,20,50,34,'AB','CD', True,False}
#
# print(set_item.pop())
# print(set_item.remove(34))
# set_item.add(33)
# print(set_item)
#
# # Set method : Compare____
#
# a = {1,2,3,4}
# b = {3,4,5,6}
#
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a.issubset(b))
# print(a.issuperset(b))
#
# print({40,2,4,7})
#
#
# # Dictionaries Data_type
#
# empty_dict = {}
#
# dict_example = {'key1': 'value2','key2': 'value2'}
# print(dict_example)
#
# st = {7,6,0,1}
# print(st)
#
# dict = {'a': 1, 'b': 2, 'c': 3}
# print(dict['a'])
#
# you = (1,2,3,4)
#
# dict['a'] = 67
# print(dict)
# print(type(you))
#
# a = 'Hello'
# print(a[1])
#
# first_v = int('23')
# second_v = float('23.89')
# print(first_v + second_v)
#
# my_name = 'Million'
# print(my_name[0])
# print(len(my_name))
#
# num_list_4 = [1,2,3,4,5,6]
# num_list_4.reverse()
# num_list_4.append('wood')
# num_list_4.extend([7,8,9])
# num_list_4 += [0,0,0]
# print(num_list_4)
# num_list_4[2] = 100
# print(num_list_4)
#
# colors = ('red','green','blue')
# print(colors[1])
#
# st = {1,2,3,4}
# print(st)
# st.add(5)
# print(st)
#
# personal_dict = {
#     'name':'john',
#     'age':25,
# }
# print(personal_dict)
#
# personal_dict['name'] = 'Million'
# print(personal_dict)
#
# var = 10>5
# print(var)
# print(type(var))
#
#
# a  = [90,34,10,60,50,40,12]
# print(type(a))
# st  = set(a)
# print(type(st))
# BACKPACK GAME
from enum import unique, Enum
from faulthandler import is_enabled
from os import add_dll_directory

# pack = []
# print('0. Starting Journey With Empty backpack')
#
# Dash = '-'*50
#
# print('🏆', pack)
# print(Dash)
#
# # Pick up StarterKit Item.
#
# #--------------------------------------
# print('1. 📦 Picking up StarterKit (Armor, Shield, Sword, Potion)')
#
# pack.append('Armor')
# pack.append('Sword')
# pack.append('Shield')
# pack.append('Potion')
#
# print('🏆', pack)
# print(Dash)
#
# # Loot a Treasure Chest
# #------------------------------------------
#
# print('2. 🎁 Looting a Treasure Chest')
# Chest    = ['Map', 'Potion', 'Compass', 'Potion']
#
# print(f'Chest: {Chest}')
#
# pack.extend(Chest) # or backpack += Chest
# print('🏆', pack)
# print(Dash)
#
#
#
# # Visit Merchant
# #-------------------------------
#
# print('3. 🤳 Visiting Merchant')
# print('-Selling the Shield')
# print('-Upgrading Sword -> Magic GreatSword')
#
# pack.remove('Shield')
# inx         = pack.index('Sword')
# pack[inx] = 'Magic GreatSword'
#
# print('🏆', pack)
# print(Dash)
#
# # check Inventory------
#
# print('4. 🔭 Checking backpack')
# print('🏆', pack)
#
# total_count = len(pack)
# unique_count = len(set(pack))
# potion_count = pack.count('Potion')
#
# print(f'There are {total_count} items in backpack')
# print(f'There are {unique_count} unique items in backpack')
# print(f'There are {potion_count} potion items in backpack')
#
#
# # Dropped the Backpack.------------
# #------------------------------------
# print('5. 🙃 Dropped the backpack Upside-Down...')
# pack.reverse()
#
# print('🏆', pack)
# print(Dash)
#
# # Sorting Items ---
# #-------------------------------------
# print('6. ➡️Sorting')
# pack.sort()
# # backpack.sort(key=len)
#
# print('🏆', pack)
# print(Dash)
#
# # 3 Items Stolen During Sleep
# #----------------------------------------
#
# print('7. 💤Sleeping...')
#
# a      = pack.pop()
# b      = pack.pop(2)
# c      = pack.pop()
#
# stolen = [a,b,c]
# print(f'Stolen Items: {stolen}')
# print('🏆', pack)
# print(Dash)
#
# # 8️⃣ Found Magic-ring
# #------------------------------
# print('8. 💍Found Magic Ring And Coin Pouch')
# ring = 'Magic Ring'
# coin_pouch = ['Gold Coin', 'Silver Coin']
#
# pack.insert(0, ring)
# pack.append(coin_pouch)
#
# print('🏆', pack)
# print(Dash)
#
# # 9️⃣ Half backpack Contents Have Teleported
# #--------------------------------
# print('9. 💥 Half Items Magically Disappeared. Damn You Magic Ring...')
#
# count = len(pack)
# half = count//2 # or half = int(count/2)
# pack = pack[:half]
#
# print('🏆', pack)
# print(Dash)
#
# # 🔟 Bandits Stole Empty Backpack
# #---------------------------
# print('10. 💸 Bandit Attacked.')
# print('Backpack Stolen...')
#
#
# pack = None
#
# print('🏆', pack)
# print(Dash)

# Dict -----------------------------------------------

#Dict  ----------------------
# phonebook = {
#     'Ricky': '+43 4111 6122',
#     'Tommy': '+43 7655 6222',
#     'Kamal': '+43 0010 1110'
# }
#
# # Add more item
#
# phonebook['Erik'] = '+372 8999 4111'
# phonebook['Kristina'] = '+372 5454 9700'
# phonebook['Theo'] = '+372 9494 7070'
#
# print(phonebook)
# number = phonebook['Erik']
#
# print(f'📞 Calling Erik...({number})')
#
# # Level Two dict(Advanced)
#
# player = {
#     'Name'     : 'Erik',
#     'Class'    : 'Warrior',
#     'Health'   : 100,
#     'Level'    : 1,
#     'Backpack' : []
# }
#
# # Modify status---------------
#
# player['Level'] += 1
# print(player)
#
# # Add Item-----------------------
#
# player['Backpack'].append('Item-A')
# player['Backpack'].append('Item-B')
# player['Backpack'].append('Item-C')
# player['Backpack'].append([10,20,[21,22,23,24],30])
#
# for k, v in player.items():
#     print(k, v)


# Basic Python Operation----------------------

# Lesson 06---------

# x = 10
# y = 20
# z = x +y
# print(z)
# # Join Strings
# a = 'Hello '
# b = 'World'
# c = a + b
# print(c)
#
# name = 'Million'
# print('My name is ' + name)
#
# # Multiply Strings
#
# print('Hello')
# print('-'*100)
# print('Hello\n'*3)
#
#
# # Membership operator
#
# # message = 'We need to build a brick wall'
# #
# # print('brick' in message) #True
# # print('wal' in message)   #True
# # print('glass' not in message) #True
# # print('need' not in message)
#
#
# # Equal / Not Equal operators
#
# a = 'Concrete-10cm'
# b = 'Concrete-20cm'
#
# print(a==b)
# print(a!=b)
#
# print(104 ** 4)
#
# #List Operator
#
# mats_1 = ['Concrete', 'Steel', 'Glass']
# mats_2 = ['Wood','Bricks']
# mats_3 = mats_1 + mats_2 # mats_1.extend(mats_2)
# print(mats_3)
#
# print(mats_1*3)
#
# print(mats_2 in mats_3)
#
#
# # Numerical Operator
#
# print(6**2)
#
# # Equality
# print(mats_1 == mats_2)

# It's Time to add logic to python

#--------------1--------Logic syntax Basics-----
condition = 5 < 0

# if condition:
#     print('Code A')
#     print('Code B')
#     print('Code C')
#
# #----Example If/Elif/Else
#
# temp = -20
#
# if temp > 25:
#     print("It's really hot outside ♨️😎")
# elif temp > 15:
#     print("It's warm outside")
# elif temp > 0:
#     print("It's chill outside")
# else:
#     print("It's freezing outside")
#
# # Logical Operator
# #------and,  or.     not
#
# x = 20
# y = 40
#
# if x > 0 and x < 100 and y > 0 and y < 100:
#     print('X coordinate is Good')
#     print('Y coordinate is Good')
#
# is_enabled = True
#
# if not is_enabled:
#     print('All Good!')
# # Membership Operator ---in,  not in ->
# # Nested Statement
#
# panel_W = 900
# panel_H = 3500
#
# if panel_W <= 1500:
#     print('Width is Good ')
#     if panel_H <= 3000:
#         print('Height is Good ')
#     else:
#         print('Height is not Good')
# else:
#     print('Width is not Good')

# Exercise

           #user Input---
#
# color1 = input('Enter First Color (red, blue, yellow): ').lower()
# color2 = input('Enter Second Color (red, blue, yellow): ').lower()
# color = [color1, color2]
# print('-'*50)
# print(f"🥼 Let's Mix {color1} and {color2}\n")
# if color1 == color2:
#     emoji = ''
#     if color1 == 'red':
#         emoji = '❤️'
#     elif color1 == 'blue':
#         emoji = '💙'
#     elif color1 == 'yellow':
#         emoji = '💛'
#     print("🎨 You're using the same color!")
#     print(f'🧪{color1} + 🧪{color2} = {color1} {emoji}.')
# elif 'red' in color and 'blue' in color:
#     print(f'🧪{color1} + 🧪{color2} = Purple 💜.')
# elif 'red' in color and 'yellow' in color:
#     print(f'🧪{color1} + 🧪{color2} = Orange 🧡.')
# elif 'blue' in color and 'yellow' in color:
#     print(f'🧪{color1} + 🧪{color2} = Green 💚.')
# else:
#     print('❌ Invalid Color Combination. \nPlease use red, blue or yellow')

# field = input("Please inter your field of study: ").lower()
# if field  in ['social', 'natural']:
#     agreement = input(f"Do you want to check your {field}?: ").lower()
# if field == 'natural' and agreement == 'yes':
#     print('Please fill the following subjects')
#     maths = float(input('Maths: '))
#     physics = float(input('physics: '))
#     biology = float(input('Biology: '))
#     chemistry = float(input('Chemistry: '))
#     english = float(input('English: '))
#     total = maths + physics + biology + chemistry + english
#     total = float(total)
#     print(f'total is: {total}')
#     average = total / 5
#     print(f'Average: {total / 5}')
#     if total >= 299:
#         print(f'Congratulation You Passed! With Average: {average}')
#     else:
#         print(f'Ooh You Failed! With Average: {average}')
# elif field == 'social' and agreement == 'yes':
#     print('Please fill the following subjects')
#     history = float(input('History: '))
#     geography = float(input('Geography: '))
#     english = float(input('English: '))
#     citizenship = float(input('Citizenship: '))
#     maths = float(input('Maths: '))
#     total = maths + english + citizenship + history + geography
#     print(f'Total is: {total}')
#     average = total / 5
#     print(f'Average: {total / 5}')
#     if total >= 299:
#         print(f'Congratulation You Passed! With Average: {average}')
#     else:
#         print(f'Ooh You Failed! With Average: {average}')
# elif field == 'social' and agreement == 'no' or field == 'natural' and agreement == 'no' or field != 'social' or field != 'natural':
#     print('Please insert a valid field')
#     want = input('do you want to continue?').lower()





# maths = float(input('Maths: '))
# biology = float(input('Biology: '))
# total = maths + biology
#
# print(total)

numbers = [1, 2, 3, 2, 4, 1, 5]

for n in numbers:
    count = numbers.count(n)
    if count > 1:
        print(n)

# Swap two variables without temp variable.
a = 10
b = 20

a, b = b, a 

print(a)  # 20
print(b)  # 10