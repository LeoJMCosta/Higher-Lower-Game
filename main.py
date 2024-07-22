from art import logo
from art import vs
from game_data import data
import random

print(logo)

def counter():
    score = 0
    initial_counter = random.choice(data)

    name = initial_counter['name']
    follower_count1 = initial_counter['follower_count']
    description = initial_counter['description']
    country = initial_counter['country']
    print(f"Compare A: {name}, a {description}, from {country}")

    print(vs)

    vs_counter = random.choice(data)

    name = vs_counter['name']
    follower_count2 = vs_counter['follower_count']
    description = vs_counter['description']
    country = vs_counter['country']
    print(f"Againt B: {name}, a {description}, from {country}")

    if follower_count1 > follower_count2:
        score += 1
        print(score)


counter()