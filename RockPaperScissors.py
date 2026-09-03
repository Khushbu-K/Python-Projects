import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Game_Images = [rock,paper,scissors]

Computer_Choice = random.randint(0,2)
print("Computer Chose: ")
# print(f"Computer Chose {Computer_Choice}")
print(Game_Images[Computer_Choice])

user_choice = int(input("What do you choose?"))
print(Game_Images[user_choice])

if 3<user_choice<0:
    print("Invalid Choice.")
elif user_choice == Computer_Choice:
    print("Draw!!")
elif user_choice > Computer_Choice:
    print("You Won!!")
elif Computer_Choice > user_choice:
    print("You Lose!")
elif user_choice == 0 and Computer_Choice == 2:
    print("You Win")
else:
    print("Try some other day.")




