from os import system
from art import logo_calc

def clear():
    _ = system("clear")


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    clear()
    print(logo_calc)
    num1 = float(input("Enter a number >>> "))
    continue_calc = True

    for operator in operations:
        print(operator, end=" ")

    while continue_calc:
        chosen_operator = input("\nChoose an operator >>> ")
        calc = operations[chosen_operator]
        num2 = float(input("Enter in another number >>> "))
        answer = calc(num1, num2)
        print(f"{num1} {chosen_operator} {num2} = {answer}")
        user_command = input(f"Continue with {answer}? 'y' to continue, 'n' for new calulation 'q' to quit. \n>>> ")
        if user_command == "y":
            num1 = answer
        elif user_command == "n":
            continue_calc = False
            calculator()
        else:
            return

calculator()
