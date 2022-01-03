import random
from os import system, name

system('clear')
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor="""
    _______
---'   ____)_______
          _________)
       ____________)
      (____)
---.__(___)
"""
choices=[rock,paper,scissor]
you=int(input("Enter your choice.\n0-Rock,\n1-Paper,\n2-Scissor.\nYour choice : "))
print(f"You choice : {you}")
print(choices[you])

computer=random.randint(0,2)
print(f"Computer choice : {computer}")
print(choices[computer])

if you == computer:
    print("Its a Draw!")
elif you==0 and computer ==1:
    print("Computer Wins")
elif you==1 and computer == 2:
    print("Computer Wins")
elif you==2 and computer == 0:
    print("Computer Wins")
else:
    print("You Win!!!")