## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)
your_cards=[]
your_cards.append(random.choice(cards))
your_cards.append(random.choice(cards))
your_score = 0
for card in your_cards:
    your_score = your_score + card
dealer_cards=[]
dealer_cards.append(random.choice(cards))
dealer_cards.append(random.choice(cards))
dealer_score=0

for card in dealer_cards:
    dealer_score = dealer_score + card
os.system('clear')
print(art.logo)

def is_game_over():
    if your_score == 21:
        print("You Win! Game over")
        return True

    if dealer_score == 21:
        print("BUST!! You lose! Game over")
        return True

    if your_score >21 or dealer_score > 21:
        if your_score < dealer_score:
            print("You Win! Game over")
            return True
        else:
            print("BUST!! You lose! Game over")
            return True

    if your_score >= 16 or dealer_score >= 16:
        if your_score > dealer_score:
            print("You Win! Game over")
            return True
        else:
            print("BUST!! You lose! Game over")
            return True

    return False

game_over = is_game_over()
if not game_over:
    print(f"You cards : {your_cards} with score : {your_score}")
    print(f"Dealer cards : {dealer_cards[0]}")
else:
    print(f"You cards : {your_cards} with score : {your_score}")
    print(f"Dealer cards : {dealer_cards} with score : {dealer_score}")

while not game_over:
    choice=input("Enter 'y' to Pick a card and 'n' to pass : ")
    if choice == 'y':
        picked_card = random.choice(cards)
        if picked_card == 11:
            if your_score + picked_card > 21:
                picked_card = 1
            else:
                picked_card = 11
        your_score = your_score + picked_card
        your_cards.append(picked_card)
    else:
        if not is_game_over():
            picked_card = random.choice(cards)
            if picked_card == 11:
                if dealer_score + picked_card > 21:
                    picked_card = 1
                else:
                    picked_card = 11
            dealer_score = dealer_score + picked_card
            dealer_cards.append(picked_card)
    os.system('clear')
    print(art.logo)
    game_over = is_game_over()
    if not game_over:
        print(f"You cards : {your_cards} with score : {your_score}")
        print(f"Dealer cards : {dealer_cards[0]}")
    else:
        print(f"You cards : {your_cards} with score : {your_score}")
        print(f"Dealer cards : {dealer_cards} with score : {dealer_score}")