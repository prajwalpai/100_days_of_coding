# Import Libraries

# Create Menu of beverages
import os
import art

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Update Resources
choice = "ON"
money_earned = 0
resources = {
    "water": 300,
    "milk": 150,
    "coffee": 100,
}



#
def report_machine_status():
    print("\nThe Current stock update : ")
    print("==========================")
    for k,v in resources.items():
        print(f"{k}\t: {v}")
    print(f"Money\t: {money_earned}")
    print("==========================\n")
    print("\nReloading Menu...\n")
    os.system('sleep 10')
    return

def check_stock(choice):
    for k,v in MENU[choice]['ingredients'].items():
        if (resources[k] < v):
            print(f"Sorry there is not enough {k}")
            return False
    return True

def take_money(choice):
    global money_earned
    quarter = 0.25 * int(input("how many quarters?\t: "))
    dimes   = 0.10 * int(input("how many dimes?  \t: "))
    nickel  = 0.05 * int(input("how many nickles?\t: "))
    pennies = 0.01 * int(input("how many pennies?\t: "))
    money_in_dollar= quarter+dimes+nickel+pennies
    print(f"Money you gave \t: {money_in_dollar}")
    if money_in_dollar < MENU[choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change=money_in_dollar - MENU[choice]['cost']
        print(f"Take your change : {round(change, 2)}")
        money_earned = money_earned + MENU[choice]['cost']
    return True

def make_coffee(choice):
    global resources
    for k,v in MENU[choice]['ingredients'].items():
        resources[k] = resources[k] - v
    return

def greet(choice):
    print(f"\nEnjoy your {choice} ☕️ ")
    print("\nReloading Menu...\n")
    os.system('sleep 7')
    os.system('clear')
    return

while not choice == 'off':
    os.system('clear')
    print(art.coffee)
    choice=input("\nWhat would you like? (espresso/latte/cappuccino) : ").lower()

    if choice == 'off':
        continue
    elif choice == 'report':
        report_machine_status()
    elif choice in MENU.keys():
        if check_stock(choice):
            if take_money(choice):
                make_coffee(choice)
                greet(choice)
    else:
        print("Invalid Choice, Think you are yet to get your first coffee!")
