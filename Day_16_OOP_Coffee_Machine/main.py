from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_off = False

cafe_menu = Menu()
cafe_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


while not machine_off:
    drink = input("Would you like to order any drink "+cafe_menu.get_items()+" : ")
    if drink == 'off':
        machine_off = True
        continue
    elif drink == 'report':
        coffee_maker.report()
        cafe_money_machine.report()
    else:
        cafe_drink = cafe_menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(cafe_drink):
            if coffee_maker.is_resource_sufficient(cafe_drink):
                if cafe_money_machine.make_payment(cafe_drink.cost):
                    coffee_maker.make_coffee(cafe_drink)
