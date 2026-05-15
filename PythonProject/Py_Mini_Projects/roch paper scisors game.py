import random

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
print(computer_choice)
while True:
    user_input = input('Rock, Paper, Scissor. (r/p/s): ').lower()
    if user_input == 'r':
        print(f'You chose 🪨!')
        print(f'Computer chose {choices[1]}!')
    elif user_input == 'p':
        print('You lose!')
    elif user_input == 's':
        print('You win!')
    else:
        print('Invalid Choice!')