from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

choices = str(menu.get_items()).split("/")
choices = choices[:-1]

def makeCoffee(option):
    item = menu.find_drink(option)
    sufficient = coffeeMaker.is_resource_sufficient(item)
    if sufficient == True:
        enoughMoney = moneyMachine.make_payment(item.cost)
        if enoughMoney == True:
            coffeeMaker.make_coffee(item)
        else:
            return
    else:
        return


def printMenu():
    num = 1
    for x in choices:
        print(x + " or " + str(num))
        num = num + 1
    print("4 for resource list")
    print("5 for machine refill")
    print("0 to exit")


def main():
    while(1):
        print("\nSelect an option")
        printMenu()
        option = input().lower()

        if option == "latte" or option == "1":
            makeCoffee("latte")
        elif option == "espresso" or option == "2":
            makeCoffee("espresso")
        elif option == "cappuccino" or option == "3":
            makeCoffee("cappuccino")
        elif option == "4":
            coffeeMaker.report()
            moneyMachine.report()
        elif option == "5":
            coffeeMaker.refill()
        elif option == "0":
            print("exiting ...")
            time.sleep(3)
            break
        else:
            print("Select a valid option")


main();