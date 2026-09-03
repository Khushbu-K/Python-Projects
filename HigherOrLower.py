import random
import art
from game_data import data

# Guess highest follower game.

print(art.logo)
ACTUAL_NUMBER1 = random.choice(data)
ACTUAL_NUMBER2 = random.choice(data)
print(ACTUAL_NUMBER1, ACTUAL_NUMBER2)

print(f"Who has more followers? {ACTUAL_NUMBER1['name']}, Press A for selection.")
print(art.vs)
print(f"Your other option is: {ACTUAL_NUMBER2['name']}. Press B for selection.")

guess1 = input("Enter Your Choice A or B: ")

def guess_game():
    if guess1 == "A":
        if ACTUAL_NUMBER1['follower_count'] > ACTUAL_NUMBER2['follower_count']:
            print(f"You WIN! The {ACTUAL_NUMBER1['name']} has {ACTUAL_NUMBER1['follower_count']}")
        elif ACTUAL_NUMBER1['follower_count'] == ACTUAL_NUMBER2['follower_count']:
            print(f"You win, both has same number of follower count.")
        else:
            print(f"You lose. The {ACTUAL_NUMBER1['name']} has"
                  f" {ACTUAL_NUMBER1['follower_count']}. "
                  f"While {ACTUAL_NUMBER2['name']} has "
                  f"{ACTUAL_NUMBER2['follower_count']}. YOU LOST!")
    else:
        if ACTUAL_NUMBER2['follower_count'] > ACTUAL_NUMBER1['follower_count']:
            print(f"You WIN! The {ACTUAL_NUMBER2['name']} has {ACTUAL_NUMBER2['follower_count']}. While the {ACTUAL_NUMBER1['name']} has {ACTUAL_NUMBER1['follower_count']}")
        elif ACTUAL_NUMBER2['follower_count'] == ACTUAL_NUMBER1['follower_count']:
            print(f"You win, both has same number of follower count.")
        else:
            print(f"You lose. The {ACTUAL_NUMBER1['name']} has"
                  f" {ACTUAL_NUMBER1['follower_count']}. "
                  f"While {ACTUAL_NUMBER2['name']} has "
                  f"{ACTUAL_NUMBER2['follower_count']}. YOU LOST!")

guess_game()