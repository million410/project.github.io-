# Guessing a number ---------------

# import random
# import traceback
#
# min_n = 1
# max_n = 10
#
# #  conditions -----
# while True:
#     secret_n = random.randint(min_n, max_n)
#     try:
#         ask_u = int(input('Guess a number: '))
#         if ask_u == secret_n:
#             print('You Got it!')
#             break
#         else:
#             print('You Lose it!')
#     except Exception as e:
#         print('Problem: ', type(e).__name__,'(',str(e), ')')
#         traceback.print_exc()
#     replay_n = input('Do you want to replay? (y/n): ').lower()
#     if replay_n != 'y':
#         print('Game over!')
#         break

def greet(name):
    print('Hello', name)
greet('Isaac')
greet('Julia')

#-------------Ask name and country and the name must be from student that takes exam only
#-------------Student must insert  their correct id number
#-------------They must choice either 'Social' or 'Natural' else the system won't work
#-------------Show student status weather good or bad, if it is bad  ask them  their special talent and give them random inspiration and motivational
#-------------Inorder to inspire it show students name(unknown) that score similar mark with him or her
#-------------At the end the system ask them are want to start again, but it stops if they ask before with that name and id
student_info = [
    {
        'name': 'Million',
        'age': 18,
        'country': 'Ethiopia',
        'field': 'social',
        'email': 'mil77@gmail.com',
        'id': '1120005'
    },
    {
        'name': 'Ebba',
        'age': 17,
        'country': 'Europe',
        'field': 'social',
        'email': 'ebbaDo@gmail.com',
        'id': '1420006'
    },
    {
        'name': 'Ismael',
        'age': 19,
        'country': 'Israel',
        'field': 'social',
        'email': 'ismael@gmail.com',
        'id': '1421006'
    },
    {
        'name': 'Kamal',
        'age': 19,
        'country': 'Turkey',
        'field': 'natural',
        'email': 'kamal@gmail.com',
        'id': '1121006'
    },
    {
        'name': 'Afghanistan',
        'age': 21,
        'country': 'Osman',
        'field': 'social',
        'email': 'osman@gmail.com',
        'id': '11211006'
    },
    {
        'name': 'Hitler',
        'age': 23,
        'country': 'Germany',
        'field': 'natural',
        'email': 'hit12@gmail.com',
        'id': '1021006'
    },
    {
        'name': 'Ephrem',
        'age': 20,
        'country': 'Ethiopia',
        'field': 'natural',
        'email': 'ephrem@gmail.com',
        'id': '0021006'
    }
]

li = ['s','p', 'l', 'i', 't']
word = 'Split or ---join'

string1 = "der Fluß"
string2 = "DER FLUSS"
print(string1.casefold())

world = 'World War'
new_world = world.replace(' War', '-Peace')
l_new_world = [l for l in new_world]
l_new_world.insert(5, 's')
l_new_world.sort(reverse=True)
print(l_new_world)
dict_l = {char: ord(char) for char in l_new_world}
print(dict_l)

copy = list('copy text.')
copied_text = copy.copy()
copied_text = [char for char in copied_text if char != ' ']
copied_text.reverse()
copied_text.clear()
print(copied_text)