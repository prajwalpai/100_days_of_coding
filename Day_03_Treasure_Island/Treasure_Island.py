print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************

Welcome to the TREASURE ISLAND

Your mission is to find the treasure
''')

direction=input("Would you like to go left/right : ")
if direction.lower() == "right":
    print("\nYou fell into a hole. GAME OVER!!\n")
else:
    action=input("\nWould you like to swim or wait : ")
    if action.lower() != 'wait':
        print("\nYou were attacked by trout. GAME OVER!!\n")
    else:
        door=input("\nWhich door will you choose? Red/Blue/Yellow : ").lower()
        if door == 'yellow':
            print("\nYou WIN!!\n")
        elif door == 'blue':
            print("\nYou are a feast for the beasts. GAME OVER!!\n")
        elif door == 'red':
            print("\nYou got burned by Fire. GAME OVER!!\n")
        else:
            print("\nGAME OVER!!\n")


