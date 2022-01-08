# import Libraries
import random
import art
import data
import os

# Global Initialisations
correct_choice = True
score = 0

# Display Higher/Lower


# Pick 2 choices to Comparre
compare_a = random.choice(data.data)


while correct_choice:
    compare_b = random.choice(data.data)
    os.system('clear')
    print(art.logo)
    print(f"\nYour Current Score = {score}")
    print(f"\nCompare A : {compare_a['name']} , a {compare_a['description']} , from {compare_a['country']} ")
    print(art.vs)
    print(f"\nCompare B : {compare_b['name']} , a {compare_b['description']} , from {compare_b['country']} ")
    choice = input("\nWho do you think has more Followers? Type 'A' or 'B' : ").lower()

    if compare_a['follower_count'] > compare_b['follower_count'] and choice == 'a':
        print("\nYou are right!! Loading next question\n")
        os.system('sleep 4')
        score += 1
        compare_a = compare_b
    elif compare_a['follower_count'] < compare_b['follower_count'] and choice == 'b':
        print("\nYou are right!! Loading next question\n")
        os.system('sleep 4')
        score += 1
        compare_a = compare_b
    elif compare_a['follower_count'] == compare_b['follower_count']:
        print('\nYou are right!! Loading next question\n')
        os.system('sleep 4')
        score += 1
        compare_a = compare_b
    else:
        correct_choice = False
        os.system('clear')
        print(art.game_over)
        print(f"\n\nYou got that wrong!! Your Final score was = {score}\n\n")

