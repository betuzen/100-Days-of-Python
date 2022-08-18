import day15Dictionary
import time

#Importing dictionary
coffee = day15Dictionary.MENU
machine = day15Dictionary.resources


def printReport():
    print("Water: " + str(machine["water"]))
    print("Milk: " + str(machine["milk"]))
    print("Coffee: " + str(machine["coffee"]))
    print("Money: " + str(machine["money"]) + "\n")


def createCoffee(option, totalMoney):
    machine["water"] = machine["water"] - coffee[option]["ingredients"]["water"]
    machine["milk"] = machine["milk"] - coffee[option]["ingredients"]["milk"]
    machine["coffee"] = machine["coffee"] - coffee[option]["ingredients"]["coffee"]
    machine["money"] = machine["money"] + totalMoney


def addTotal(moneyInserted, totalMoney):
    return (moneyInserted + totalMoney)

def giveChange(totalMoney, moneyNeeded):
    print("Calculating Change")
    for x in range(3):
        time.sleep(2)
    change = abs(totalMoney - moneyNeeded)
    machine["money"] = machine["money"] - change
    print("Your change is: " + str(change))


def checkTotal(totalMoney, moneyNeeded, option):
    if totalMoney >= moneyNeeded:
        print("Enough Money Inserted!")
        print("Making Coffee!")
        for x in range(3):
            print("...")
            time.sleep(1)
        createCoffee(option, totalMoney)
        giveChange(totalMoney, moneyNeeded)

    else:
        print("You need a total of " + str(moneyNeeded - totalMoney))


def insertCoins(option):
    moneyNeeded = coffee[option]["cost"]
    totalMoney = 0

    while(1):
        if totalMoney >= moneyNeeded:
            break
        print("insert coins")
        print("Money Needed: " + str(moneyNeeded))
        print("1: Penny = $0.01")
        print("2: Nickel = $0.05")
        print("3: Dime = $0.10")
        print("4: Quarter = $0.25")
        print("5: Half Dollar = $0.50")
        print("6: Dollar = $1.00")
        print("0: Cancel Operation")
        moneyInsert = input("")

        if moneyInsert == "1":
            print("Penny Inserted")
            totalMoney = addTotal(0.01, totalMoney)
            checkTotal(totalMoney, moneyNeeded, option)

        elif moneyInsert == "2":
            print("Nickel Inserted")
            totalMoney = addTotal(0.05, totalMoney)
            checkTotal(totalMoney, moneyNeeded, option)

        elif moneyInsert == "3":
            print("Dime Inserted")
            totalMoney = addTotal(0.10, totalMoney)
            checkTotal(totalMoney, moneyNeeded, option)

        elif moneyInsert == "4":
            print("Quarter Inserted")
            totalMoney = addTotal(0.25, totalMoney)
            checkTotal(totalMoney, moneyNeeded, option)

        elif moneyInsert == "5":
            print("Half Dollar Inserted")
            totalMoney = addTotal(0.50, totalMoney)
            checkTotal(totalMoney, moneyNeeded, option)

        elif moneyInsert == "6":
            print("Dollar Inserted")
            totalMoney = addTotal(1.00, totalMoney)
            checkTotal(totalMoney, moneyNeeded, option)

        elif moneyInsert == "0":
            print("Cancelling Operation")
            break

        else:
            print("Invalid Option")

def checkResources(option):
    print("Checking Resources")
    if machine["water"] < coffee[option]["ingredients"]["water"]:
        print("Not Enough Water")
    if machine["milk"] < coffee[option]["ingredients"]["milk"]:
        print("Not Enough Milk")
    if machine["coffee"] < coffee[option]["ingredients"]["coffee"]:
        print("Not Enough Coffee")
    insertCoins(option)

def refill():
    print("refilling machine")
    machine["water"] = machine["water"] + 250
    machine["milk"] = machine["milk"] + 250
    machine["coffee"] = machine["coffee"] + 250

def main():
    while (1):
        print("Enter your coffee option")
        print("espresso or 1")
        print("cappuccino or 2")
        print("latte or 3")
        print("cancel order or 0")

        option = input().lower()
        if option == "espresso" or option == "1":
            print("Espresso was selected")
            checkResources("espresso")
        elif option == "cappuccino" or option == "2":
            print("Cappuccino was selected")
            checkResources("cappuccino")
        elif option == "latte" or option == "3":
            print("Latte was selected")
            checkResources("latte")
        elif option == "result" or option == "4":
            print("Result was selected")
            printReport()
        elif option == "refill" or option == "5":
            refill()
        elif option == "off" or option == "0":
            print("Turning Machine Off")
            break
        else:
            print("Enter a valid option")

main()
