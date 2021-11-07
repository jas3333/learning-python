from gamedata import data
import random
from os import system
from art import vs_logo

def format_data(data):
    data = f"{data['country']}" 
    return data 
    
def clear():
    _ = system("clear")

def present_choice():
    while True:
        choice_b = random.choice(data)
        if choice_a == choice_b:
            choice_b = random.choice(data)
        return choice_b

def display_data():
    clear()
    print("A: " + format_data(choice_a))
    print(vs_logo)
    print("B: " + format_data(choice_b))

def checker(choice, choice_a, choice_b):
    if choice == "a" and choice_a["population"] > choice_b["population"]:
        choice_a = choice_b
        return choice_a
    elif choice == "b" and choice_b["population"] > choice_a["population"]:
        choice_a = choice_b
        return choice_a 
    else:
        return 

game = True
choice_a = random.choice(data)
choice_b = present_choice()
display_data()

choice = input("\nWhich has more population. [a] or [b] >>> ")
choice_a = checker(choice, choice_a, choice_b)
score = 0
if choice_a != choice_b:
    game = False
while game:
    score += 1
    choice_b = present_choice()
    display_data()
    choice = input("\nWhich has more population. [a] or [b] >>> ")
    choice_a = checker(choice, choice_a, choice_b) 
    if choice_a != choice_b:
        game = False

print(f"If you ended up here you lost... {score} was your final score.")    






























