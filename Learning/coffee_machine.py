from os import system
import time, sys

machine_data = {
    "resources": {
                    "Water": 900,
                    "Milk": 200,
                    "Coffee": 175,
                    "Money": 5.00
                 },
    "products": {
                    "Espresso": 4.00,
                    "Latte": 5.50,
                    "Cappuccino": 6.45,
                }
}


enough_money = True
enough_resources = True
quarter = .25
dime = .10
nickel = .05
penny = .01


def clear():
    _ = system("clear")


def display_product():
    num = 0
    for keys in machine_data["products"]:
        num +=1
        print(f"[{num}]{keys} -- ${machine_data['products'][keys]}")


def display_resources():
    for keys in machine_data["resources"]:
        if keys == "Water" or keys == "Milk":
            print(f"{keys}: {machine_data['resources'][keys]}ml")
        elif keys == "Money":
            print(f"{keys}: ${round(machine_data['resources'][keys], 2)}")
        else:
            print(f"{keys}: {machine_data['resources'][keys]}mg")


def enter_money(enough_money):
    money = 0

    input_quarter = int(input("Quarters: >>> "))
    money += input_quarter * quarter

    print(f"\nMoney added: ${money}")

    input_dime = int(input("Dimes: >>> "))
    money += input_dime * dime

    print(f"\nMoney added: ${money}")

    input_nickel = int(input("Nickels: >>> "))
    money += input_nickel * nickel 

    print(f"\nMoney added: ${money}")

    input_penny = int(input("Pennies: >>> "))
    money += input_penny * penny 

    print(f"\nMoney added: ${round(money, 2)}")

    if money < machine_data["products"][wanted_drink]:
        print("Sorry you didn't insert enough money.")
        print(f"Refunding: ${round(money,2)}")
        return False 
    else:
        machine_data["resources"]["Money"] += machine_data["products"][wanted_drink]
        money -= round(machine_data["products"][wanted_drink], 2)
        print(f"Your change is ${round(money,2)}")
        return True


def resource_check(enough_resources):
    if wanted_drink == "Espresso":
        if machine_data["resources"]["Water"] < 100 or machine_data["resources"]["Milk"] < 50 or machine_data["resources"]["Coffee"] < 10:
            return False 
        else:
            return True 
    if wanted_drink == "Cappuccino":
        if machine_data["resources"]["Water"] < 100 or machine_data["resources"]["Milk"] < 50 or machine_data["resources"]["Coffee"] < 10:
            return False 
        else:
            return True 
    if wanted_drink == "Latte":
        if machine_data["resources"]["Water"] < 100 or machine_data["resources"]["Milk"] < 70 or machine_data["resources"]["Coffee"] < 10:
            return False 
        else:
            return True 


while True:
    display_product()
    prompt = input("\nWhat would you like? ")


    if prompt == "resources" or prompt == "res":
        display_resources()
    

    elif prompt == "shutdown now":
        print("Shutting down....")
        time.sleep(3)
        sys.exit()


    elif prompt == "1" or prompt == "espresso":
        wanted_drink = "Espresso"
        enough_resources = resource_check(enough_resources)
        if enough_resources == True:
            enough_money = enter_money(enough_money)
            if enough_money == True:
                print(f"Making a {wanted_drink}")
                machine_data["resources"]["Water"] -= 100
                machine_data["resources"]["Milk"] -= 50
                machine_data["resources"]["Coffee"] -= 10
                time.sleep(2)
                print(f"Your {wanted_drink} is ready. Becareful it's hot...")
                time.sleep(3)
                clear()
            else:
                print("Sorry, you didn't put enough money in. Try again.")
                time.sleep(3)
                clear()
        else:
            print("Not enough resources, please refill.")
            time.sleep(3)
            clear()


    elif prompt == "2" or prompt == "latte":
        wanted_drink = "Latte"
        enough_resources = resource_check(enough_resources)
        if enough_resources == True:
            enough_money = enter_money(enough_money)
            if enough_money == True:
                print(f"Making a {wanted_drink}")
                machine_data["resources"]["Water"] -= 100
                machine_data["resources"]["Milk"] -= 70
                machine_data["resources"]["Coffee"] -= 10
                time.sleep(2)
                print(f"Your {wanted_drink} is ready. Becareful it's hot...")
                time.sleep(3)
                clear()
            else:
                print("Sorry, you didn't put enough money in. Try again.")
                time.sleep(3)
                clear()
        else:
            print("Not enough resources, please refill.")
            time.sleep(3)
            clear()


    elif prompt == "3" or prompt == "cappuccino":
        wanted_drink = "Cappuccino"
        enough_resources = resource_check(enough_resources)
        if enough_resources == True:
            enough_money = enter_money(enough_money)
            if enough_money == True:
                print(f"Making a {wanted_drink}")
                machine_data["resources"]["Water"] -= 100
                machine_data["resources"]["Milk"] -= 50
                machine_data["resources"]["Coffee"] -= 10
                time.sleep(2)
                print(f"Your {wanted_drink} is ready. Becareful it's hot...")
                time.sleep(3)
                clear()
            else:
                print("Sorry, you didn't enter enough money in. Try again.")
                time.sleep(3)
                clear()
        else:
            print("Not enough resources, please refill.")
            time.sleep(3)
            clear()

