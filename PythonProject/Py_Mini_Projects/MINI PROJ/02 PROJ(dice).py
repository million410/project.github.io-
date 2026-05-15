import random
def roll():
    min_v = 1
    max_v = 6
    roll = random.randint(min_v,max_v)
    return roll
while True:
    player = input('Enter the number of players: ')
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print('Must be between 1 - 5 players.')
    else:
        print('Invalid input. Try again.')
max_score = 50
player_score = [0 for _ in range(player)]

while max(player_score) <= max_score:
    for player_idx in range(player):
        print('\nPlayer number', player_idx + 1, 'turn has just started!\n')
        current_score = 0
        while True:
            should_roll = input('Would you like to roll (y) ').lower()
            if should_roll != 'y':
                break

            value = roll()
            if value == 1:
                print('You rolled a 1! Turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print('You rolled a:', value)

            print('Current score:', current_score)

        player_score[player_idx] += current_score
        print('Your total score is:', player_score[player_idx])

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print('Player number', winning_idx + 1, 'is the winner with a score of:', max_score)