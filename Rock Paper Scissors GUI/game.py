# --- coding: utf-8 ---
# @FileName  :game.py
# @Time      :1/9/2023 2:37 PM
# @Author    :Abraham
# @Software  :PyCharm

import random

# Create a list of play options
play = ["Rock", "Paper", "Scissor"]
# Assign a random play to the computer
computer = play[random.randint(0, 2)]


# score
player_score = 0
computer_score = 0
game_over = False

# Create game logic using while loop
while not game_over:
    # Set the player to True
    player = input("Enter your choice: Rock(R), Paper(P) or Scissor(S)?")
    if player not in ["Rock", "Paper", "Scissor"]:
        print("That's not a valid input. Check your spelling!")
    else:
        print(f"Computer chooses: {computer}")
        if player == "Rock" and computer == "Scissor":
            player_score += 1
            print(f"Player wins, Score: {player_score}")
        elif player == "Paper" and computer == "Rock":
            player_score += 1
            print(f"Player wins, Score: {player_score}")
        elif player == "Scissor" and computer == "Paper":
            player_score += 1
            print(f"Player wins, Score: {player_score}")
        if computer == "Rock" and player == "Scissor":
            computer_score += 1
            print(f"Computer wins, Score: {computer_score}")
        elif computer == "Paper" and player == "Rock":
            computer_score += 1
            print(f"Computer wins, Score: {computer_score}")
        elif computer == "Scissor" and player == "Paper":
            computer_score += 1
            print(f"Computer wins, Score: {computer_score}")
        elif player == computer:
            print("The game is a Tie")
    play_again = input("Do you want to play again(Yes/No): ")
    if play_again == "yes":
        game_over = False
        computer = play[random.randint(0, 2)]
    elif play_again not in ["Yes", "No"]:
        print("Invalid input, please check the spelling of your input!")
    else:
        game_over = True





