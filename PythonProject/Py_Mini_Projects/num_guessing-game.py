import random

number_to_guess = random.randint(1,100)
#loop
counter = 0

while True:
    try:
        user_input = input('Guess a number between 1 and 100: ')
        guess = int(user_input)
        counter += 1
        if guess < number_to_guess:
            print('Too low')
        elif guess > number_to_guess:
            print('Too high')
        else:
            print('Congratulation! You guessed the number!')
            print(f'Within {counter} guesses')
            break
    except ValueError:
        print('Please enter a number')
