from art import logo
from art import vs
from game_data import data
import random

print(logo)

score = 0

flag = False

initial_counter = random.choice(data)

while not flag:
    vs_counter = random.choice(data)

    while vs_counter == initial_counter:
        vs_counter == random.choice(data)

    print(f"Compare A: {initial_counter['name']}, a {initial_counter['description']}, from {initial_counter['country']}")
    print(vs)
    print(f"Against B: {vs_counter['name']}, a {vs_counter['description']}, from {vs_counter['country']}")

    guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    if (guess == 'a' and initial_counter["follower_count"] > vs_counter["follower_count"]) or \
       (guess == 'b' and vs_counter["follower_count"] > initial_counter["follower_count"]):
        score += 1
        print(f"You're right! Current score: {score}")
        if guess == 'a':
            initial_counter = initial_counter  # No change needed
        else:
            initial_counter = vs_counter
    else:
        print(f"Sorry, that's wrong, your final score is: {score}")
        restart = input('Do you wanna play another game? "Yes" or "No" ').lower()
        if restart == 'yes':
            score = 0
        elif restart == 'no':
            flag = True