# computer score
# user score
# tie and user winner
'''between'''
# def rock_paper_scissors():
#     computer_score = 0
#     player_score = 0
#     print("Rock Paper Scissors")
#     possible_choice = ['rock', 'paper', 'scissors']
#     while True:
#         computer_choice = possible_choice[random.randint(0, 2)]
#         user_choice = input("Enter your choice(r/p/s), press q to quit: ").lower()
#         valid_choices = ['r', 'p', 's', 'rock', 'scissors', 'paper']
#         if user_choice not in valid_choices and user_choice != 'q':
#             print(f"Invalid choice. Please choose from {', '.join(valid_choices)}")
#         elif user_choice == 'q':
#             print('You stopped playing')
#             print('Result---------')
#             print(f'You win {player_score} times and computer win {computer_score} times')
#             break
#         else:
#             if (user_choice == 'r' or user_choice == 'rock') and computer_choice == 'scissors':
#                 player_score += 1
#                 print(f"You win!: computer chose: {computer_choice}")
#             elif (user_choice == 'p' or user_choice == 'paper') and computer_choice == 'rock':
#                 player_score += 1
#                 print(f"You win!: computer chose: {computer_choice}")
#             elif (user_choice == 's' or user_choice == 'scissors') and computer_choice == 'paper':
#                 player_score += 1
#                 print(f"You win!: computer chose: {computer_choice}")
#             elif computer_choice[0] == user_choice[0]:
#                 print("Draw")
#                 print(f"Computer chose: {computer_choice}")
#             else:
#                 print(f'you lose: computer chose {computer_choice}')
#                 computer_score += 1


# rock_paper_scissors()

import random
import csv
import os


def get_user_choice():
    """Get validated user input."""
    while True:
        user_input = input("Choose (r/p/s) or q to quit: ").lower()

        if user_input == 'q':
            return 'q'

        if user_input in ['r', 'p', 's']:
            return user_input

        print("Invalid choice. Try again.")


def determine_winner(user_choice, computer_choice):
    """Return 'win', 'lose', or 'draw'."""
    if user_choice == computer_choice:
        return 'draw'

    winning_cases = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if winning_cases[user_choice] == computer_choice:
        return 'win'

    return 'lose'


def calculate_win_rate(player, computer, ties):
    total = player + computer + ties
    if total == 0:
        return 0
    return round((player / total) * 100, 2)


def save_scores(player, computer, ties, win_rate):
    filename = "scores.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)

        # Write header only if file doesn't exist
        if not file_exists:
            writer.writerow(['player_score', 'computer_score', 'ties', 'win_rate'])

        writer.writerow([player, computer, ties, win_rate])

    print("Scores saved successfully.")


def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    short_to_full = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    player_score = 0
    computer_score = 0
    ties = 0
    move_counter = {'r': 0, 'p': 0, 's': 0}

    print("=== Rock Paper Scissors ===")

    while True:
        user_input = get_user_choice()

        if user_input == 'q':
            break

        move_counter[user_input] += 1

        user_choice = short_to_full[user_input]
        computer_choice = random.choice(choices)

        result = determine_winner(user_choice, computer_choice)

        print(f"Computer chose: {computer_choice}")

        if result == 'draw':
            ties += 1
            print("Draw!")
        elif result == 'win':
            player_score += 1
            print("You win!")
        else:
            computer_score += 1
            print("You lose!")

        win_rate = calculate_win_rate(player_score, computer_score, ties)

        print("------------------------------------")
        print(f"Score → You: {player_score} | Computer: {computer_score} | Ties: {ties}")
        print(f"Win Rate: {win_rate}%")
        print("------------------------------------\n")

    # ===== End Game Summary =====
    print("\n=== Game Over ===")
    win_rate = calculate_win_rate(player_score, computer_score, ties)

    most_used_short = max(move_counter, key=move_counter.get)
    most_used_full = short_to_full[most_used_short]

    print(f"Final Score → You: {player_score} | Computer: {computer_score} | Ties: {ties}")
    print(f"Final Win Rate: {win_rate}%")
    print(f"Most Used Move: {most_used_full}")

    save_choice = input("Do you want to save this result? (y/n): ").lower()
    if save_choice == 'y':
        save_scores(player_score, computer_score, ties, win_rate)


rock_paper_scissors()


