# --- coding: utf-8 ---
# @FileName  :game.py
# @Time      :11/13/2022 10:32 PM
# @Author    :Abraham
# @Software  :PyCharm

from game_data import data
import random
from art import logo, vs
import os
from time import sleep


# Generate a random account from the game data.
def get_random_account():
    random_account = random.choice(data)
    return random_account


# random_account = get_random_account(data)
# print(random_account)
# print(random_account["name"])
# print(random_account["follower_count"])
# print(random_account["description"])
# print(random_account["country"])


# Format account data into printable format.
def format_data(data):
    account_name = data["name"]
    # follower_count = data["follower_count"]
    description = data["description"]
    country = data["country"]
    return f"{account_name} {description} from {country}"


def play_game():
    print(logo)
    account_a = get_random_account()
    account_b = get_random_account()
    answer = ""
    score = 0
    game_over = False
    while not game_over:
        while account_a == account_b:
            account_b = get_random_account()
        # print(account_a, account_b)
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        # Get follower count.
        account_a_follower = account_a["follower_count"]
        account_b_follower = account_b["follower_count"]
        user_guess = input("Who has more followers? type 'A' or 'B': ").lower()
        # If Statement to compare account follower
        if account_a_follower > account_b_follower:
            answer = "a"
        elif account_a_follower < account_b_follower:
            answer = "b"
        print(logo)
        # Check if user is correct
        if user_guess == answer.lower():
            score += 1
            account_a = account_b  # make b the next a
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


play_game()
