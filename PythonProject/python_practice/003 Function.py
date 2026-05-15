# Function in python--------------->


# syntax Basics
# def say_hello():
#     print('Hello BIM World!')
# say_hello()
#
# # Function With Argument/Parameters
# def greet(name='Erick'):
#     print('Hello {}'.format(name))
# greet('Isaac')
# greet('Ismael')
# greet()
#
# def gre(name, salutation):
#     print('hello {}{}.' .format(salutation, name))
# gre('Ismael', 'Mr.')

# 3 Return Value
bo = 'hello'
# def add_num(a, b):
#     total = a + b
#     print('{} + {} = {}'.format(a,b,total))
#
# add_num(34, 21)
#
# def user(num_1='', num_2=''):
#     num_1 = int(input('Insert First Number: '))
#     num_2 = int(input('Insert Second Number: '))
#     print(f'here is the product {num_1 * num_2}:')
# user()

# System I want to build
#-------------Ask name and country and the name must be from student that takes exam only
#-------------Student must insert  their correct id number
#-------------They must choice either 'Social' or 'Natural' else the system won't work
#-------------Show student status weather good or bad, if it is bad  ask them  their special talent and give them random inspiration and motivational
#-------------Inorder to inspire it show students name(unknown) that score similar mark with him or her
#-------------At the end the system ask them are want to start again, but it stops if they ask before with that name and id


# Let's Go -->
'filed'
#
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
# inspire_exam_passer = ['Stay consistence', '']
# inspire_exam_failer = ['book']
#
#
#

# name = input('Enter your name: ')
# id_num = input('Enter your id: ')
# count = 0
# for info in student_info:
#    count += 1
#    print(count)
#    if info['name'] != name and info['id'] != id_num:
#              again = int(input('Your Info Is Unknown, to try again press 1 only: '))
#              if again != 1:
#                  continue
#    elif info['name'] == name and info['id'] == id_num:
#          field = input('Congratulation! you signed In successfully, do you want to known all about this student? ').lower()
#          if field == 'yes':
#              print(info)
#              print(f"Now fill the following {info['field']} subjects to know your status")
#              if info['field'] == 'social':
#                   history = int(input('History: '))
#                   geography = int(input('Geography: '))
#                   citizenship = int(input('Citizenship: '))
#                   economics = int(input('Economics: '))
#                   english = int(input('English: '))
#                   total_s = history + geography + citizenship + economics + english
#                   average = total_s / 5
#                   print(f'The average score is {average}')
#                   print(f'Your total score is {total_s}')
#                   if total_s < 250:
#                       print(f'Sorry, your score under 250, you do not pass!')
#                       print('But, No worry, the more you fail the more you become strong!')
#                   else:
#                       print('ohh congratulation! you passed!')
#              elif info['field'] == 'natural':
#                    maths = int(input('Maths: '))
#                    physics = int(input('Physics: '))
#                    chemistry = int(input('Chemistry: '))
#                    biology = int(input('Biology: '))
#                    agricultural = int(input('Agricultural: '))
#                    total_n = maths + physics + chemistry + biology + agricultural
#                    average = total_n / 5
#                    print(f'The average score is {average}')
#                    print(f'Your total score is {total_n}')
#                    if total_n < 250:
#                       print(f'Sorry, your score under 250, you do not pass!')
#                       print('But, No worry, the more you fail the more you become strong!')
#                    else:
#                       print('ohh congratulation! you passed!')
#                       break
#              else:
#                print('Please enter a valid option')
#                break
#
#
#
#



#------------Dice roll

# import random
# print('Rolling Dice Game')
# counter = 0
# num     = int(input('How many dice would you roll?: '))
# while True:
#     choice = input('Roll dice?, (y/n): ').lower()
#     if choice == 'y':
#         die_1 = random.randint(1, 6)
#         die_2 = random.randint(1, 6)
#         print(f'({die_1},{die_2})')
#         counter += 1
#         print(f'You rolled {counter} time')
#         if counter == num:
#             print('Thank you for playing')
#             break
#     elif choice == 'n':
#         print('Thank you for playing')
#         break
#     else:
#         print('Invalid choice')


name = input('Enter your name: ')
id_num = input('Enter your id: ')

found = False  # flag to track match

for info in student_info:
    if info['name'] == name and info['id'] == id_num:
        found = True
        field = input(
            'Congratulations! You signed in successfully. '
            'Do you want to know all about this student? '
        ).lower()

        if field == 'yes':
            print(info)
            print(f"Now fill the following {info['field']} subjects to know your status")

            if info['field'] == 'social':
                history = int(input('History: '))
                geography = int(input('Geography: '))
                citizenship = int(input('Citizenship: '))
                economics = int(input('Economics: '))
                english = int(input('English: '))

                total = history + geography + citizenship + economics + english
                average = total / 5

            elif info['field'] == 'natural':
                maths = int(input('Maths: '))
                physics = int(input('Physics: '))
                chemistry = int(input('Chemistry: '))
                biology = int(input('Biology: '))
                agricultural = int(input('Agricultural: '))

                total = maths + physics + chemistry + biology + agricultural
                average = total / 5

            else:
                print('Invalid field')
                break

            print(f'Total score: {total}')
            print(f'Average score: {average}')

            if total < 250:
                print('Sorry, you did not pass.')
                print('Failure is part of growth.')
            else:
                print('Congratulations! You passed.')

        break  # stop searching once found

if not found:
    print('Your information is unknown. Please try again.')





