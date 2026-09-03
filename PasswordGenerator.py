import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwor = ""

# EASY METHOD:
# for i in range(0, nr_letters):
#     passwor += random.choice(letters)
#
# for i in range(0, nr_symbols):
#     passwor += random.choice(symbols)
#
# for i in range(0, nr_numbers):
#     passwor += random.choice(numbers)
#
# string_choice = random.choice(letters)
# int_choice = random.choice(numbers)
# symbols_choice = random.choice(symbols)
#
# print(passwor)

# HARD METHOD
passwrd_list = []
for i in range(0, nr_letters):
    passwrd_list.append(random.choice(letters))
for i in range(0, nr_numbers):
    passwrd_list.append(random.choice(numbers))
for i in range(0, nr_symbols):
    passwrd_list.append(random.choice(symbols))

random.shuffle(passwrd_list)
print(passwrd_list)

ypassword = ""
for char in passwrd_list:
    ypassword += char
print(f"Your password is: {ypassword}")



