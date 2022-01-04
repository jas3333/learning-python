import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '*', '+', '(', ')']

password_temp = [] 
password = ""
letter_size = int(input("How many letters would you like?\n")) 
number_size = int(input("How many numbers would you like?\n"))
symbol_size = int(input("How many symbols would you like?\n"))

for letter in range(0, letter_size):
    password_temp.append(random.choice(letters))

for letter in range(0, number_size):
    password_temp.append(random.choice(numbers))

for letter in range(0, symbol_size):
    password_temp.append(random.choice(symbols))

random.shuffle(password_temp)

for chars in password_temp:
    password += chars 

print(password)


