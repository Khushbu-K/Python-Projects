import random
from art import logo

print(logo)

actual_num = random.randint(1,20)
print(actual_num)
GAME_OVER = False
USER_CHANCE = 0

def lose_chance():
    if USER_CHANCE == 0:
        print("All chances are lapsed, you lose!")
        GAME_OVER = True

while not GAME_OVER:
    lose_chance()
    level_selection = input("Do you want easy(8) or hard game(5)? E or H ? ")

#user_guess = int(input("Guess the number\n"))

    if level_selection == "E":
        user_chance = 8
    else:
        user_chance = 5

    for i in range(user_chance):
        user_guess = int(input("Guess the number\n"))
        if user_guess > actual_num:
            print("Your guess is too high.")
        elif user_guess <actual_num:
            print("Your guess is too low.")
        elif user_guess == actual_num:
            print(f"You guessed the right number: {actual_num}. You Win!")
            GAME_OVER = True
        elif user_chance == 0:
            lose_chance()


