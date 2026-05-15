#----------------------------GAME+QUIZ-----------------
# print('welcome to my computer quiz!')
#
# playing = input('Do you want to play? ')
# score = 0
#
# if playing != 'yes':
#     quit()
# print("Okay!, let's play")
# answer = input('What does CPU stands for? ').lower()
# if answer == 'central processing unit':
#     print('correct!')
#     score += 1
# else:
#     print('incorrect!')
#
# answer = input('What does GPU stands for? ').lower()
# if answer == 'graphics processing unit':
#     print('correct!')
#     score += 1
# else:
#     print('incorrect!')
#
# answer = input('What does RAM stands for? ').lower()
# if answer == 'random access memory':
#     print('correct!')
#     score += 1
# else:
#     print('incorrect!')
# print('You got ' + str((score/4) * 100) + '%')

#

# number guesses---------
'guessing gane'
# import random
# random_no = random.randint(1,10)
# guesses = 0
# while guesses < 6:
#     guesses += 1
#     user_in = input('Make a guess: ')
#     if user_in.isdigit():
#         user_in = int(user_in)
#         if user_in == random_no:
#             print(f'You got it!------in {guesses} time')
#             break
#         elif user_in > 0 and user_in < 10:
#             print(f'You got wrong!-------you have {5 - guesses} chances left')
#         else:
#             print('Please guess a number between 0 and 10.')
#     else:
#         print('Please type a number next time.')
#         continue
#     if guesses == 6:
#         print('Game Over!')
'rock paper scissors'
# import random
#
#
# user_wins     = 0
# computer_wins = 0
# options = ['rock', 'paper', 'scissors']
#
# while True:
#     rand_no = random.randint(0, 2)
#     user_input = input("Type Rock/Paper/Scissors or Q to quiz: ").lower()
#     if user_input == "q":
#         break
#     if user_input not in options:
#         continue
#     computer_pick = options[rand_no]
#
#     if user_input == "rock" and computer_pick == "scissors":
#         print(f'computer picked: {computer_pick}')
#         print("You win!")
#         user_wins += 1
#     elif user_input == 'paper' and computer_pick == "rock":
#         print(f'computer picked: {computer_pick}')
#         print("You win!")
#         user_wins += 1
#     elif user_input == "scissors" and computer_pick == "paper":
#         print(f'computer picked: {computer_pick}')
#         print("You win!")
#         user_wins += 1
#     else:
#         print(f'computer picked: {computer_pick}')
#         print("You lose!")
#         computer_wins += 1
# print('You won', user_wins, 'times')
# print('The computer', computer_wins, 'times')
# print('Goodbye!')
'choose_your_own_adventure'
# name = input('Type your name: ')
# print('Welcome', name, 'to this adventure!')
# answer = input('you are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? left/right? ').lower()
# if answer == 'left':
#     answer = input('you come to a river, you can walk around it or swim across (walk/swim)? ').lower()
#     if answer == 'walk':
#         print('You walked for many miles, ran out of water and you lost the game.')
#     if answer == 'swim':
#         print('You across and were eaten by an alligator.')
#     else:
#         print('Not a valid option')
#
# elif answer == 'right':
#     answer = input('You come to a bridge, it looks wobbly, do you want to across or head back (cross/back)? ').lower()
#     if answer == 'back':
#         print('You go back and lose.')
#     if answer == 'cross':
#         answer = input('You cross the bridge and meet a stranger. Do you want to talk to them (yes/no)? ')
#         if answer == 'yes':
#             print('You talk to the stranger and they give you gold. You WIN!')
#         elif answer == 'no':
#             print('You ignore the stranger and they are offended and you lose.')
#         else:
#             print('Not a valid option')
#     else:
#         print('Not a valid option')
#
# else:
#     print('Not a valid option')
# print('Thank you for trying!', name)
'Password manager'
from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as f:
        f.write(key)'''

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key
key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split('|')
            print('User:', user, ', Password:', fer.decrypt(passw.encode()))


def add():
    name = input('Account name: ')
    pwd  = input('password: ')
    pwd = pwd.encode()
    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd).decode() + '\n')

while True:
    mode = input('Would you like to add a new password or view existing ones (view, add)? press q to quit. ').lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode!')
        continue