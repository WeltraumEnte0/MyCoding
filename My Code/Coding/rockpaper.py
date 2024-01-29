import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Unentschieden"
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "Du gewinnst"
    
    else:
        return "Hahaha die Maschine gewinnt"

def play_game():

    choices = ['rock', 'paper', 'scissors']

    print("Let's play Rock, Paper, Scissors!")

    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

play_game()
