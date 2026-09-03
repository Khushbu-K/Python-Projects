print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

pathtogo = input("Choose left or right. ")

if pathtogo == "left":
    cards = input("Choose cards, Spade, Club, Hearts. ")
    if cards == "Spade":
        print("Game Over, You met with an accident in forest.")
    if cards == "Hearts":
        path2 = input("Ride rollercoaster or Go for Swimming. Enter Rollercoaster or Swimming")
        if path2 == "Rollercoaster":
            print("You fell down and you lost the game.")
        else:
            print("You found the treasure. You WIN!")
    if cards == "Club":
        print("You lost the game, You became a drunker.")
else:
    newway = input("Choose the Doors. Blue, Pink, Neon. ")
    if(newway == "Blue"):
        print("Congratulations! You won a free ticket to a Hot Air Balloon flight.")
    elif newway == "Pink":
        print("Congratulations!! You won a surprise gift.")
    else:
        print("Uh-Oh! Sorry! Better try luck next time!")
