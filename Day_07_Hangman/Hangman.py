import random
import life_stages
import os

word_list='''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()
chosen_word = random.choice(word_list)

display=['_' for letter in chosen_word]
print(*display)

life=6
end_of_game = False
os.system('clear')
print(life_stages.stages[life])

while not end_of_game:
    os.system('clear')
    print(life_stages.stages[life])
    print(*display)
    guess = input("\n\nGuess a letter: ").lower()
    if guess not in chosen_word:
        life=life-1
    i=0
    for letter in chosen_word:
        if letter == guess:
            display[i]=chosen_word[i]
        i=i+1

    if '_' not in display:
        end_of_game= True
        print(life_stages.won)
    if life ==0:
        end_of_game = True
        print(life_stages.lost)