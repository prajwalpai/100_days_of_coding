import os


gavel='''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''
os.system('clear')
print(gavel)
print("\nWelcome to the secret auction program.")

all_bids={}
more_bids=True

while more_bids:
    name=input("\nWhat is your name? : ")
    bid=int(input("What's your bid? : "))
    all_bids[name]=bid
    more=input("\nAre there any other bidders? Type 'yes' or 'no'. ")
    if more == 'no':
        more_bids = False
    os.system('clear')

max_bid_value=0
max_bid_key=''
for k,v in all_bids.items():
     if v > max_bid_value:
         max_bid_value=v
         max_bid_key=k

print(f"\nThe max bid is done by the person {max_bid_key} and the winning amout is {max_bid_value}\n")