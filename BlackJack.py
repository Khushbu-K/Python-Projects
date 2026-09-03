import random
import art

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    selected_card = random.choice(cards)
    return selected_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(-10)
    elif sum(cards) > 21:
        print("End of game, you lose")
    return sum(cards)

def compare(user1_score,user2_score):
    if user1_score == user2_score:
        return "Draw"
    elif user1_score == 0:
        return "User1 wins"
    elif user2_score == 0:
        return "User2 wins"
    elif user1_score > 21:
        return "You lose"
    elif user2_score > 21:
        return "You lose"
    elif user1_score > user2_score:
        return "User 1 wins"
    elif user2_score > user1_score:
        return "User 2 wins."
    else:
        return "you lose."

def play_game():
    print(art.logo)
    game_over = False
    user1 = []
    user2 = []

    for _ in range(2):
        user1.append(deal_cards())
        user2.append(deal_cards())

    while game_over == False:
        user1_score = calculate_score(user1)
        user2_score = calculate_score(user2)
        print(f" Your first card: {user1} and score is {user1_score}")
        print(f"User 2 first score: {user2} and score is {user2_score}")

        if user1_score == 0 or user2_score == 0:
            game_over = True
        else:
            user1_draw_continue = input("Draw another card? y or n? ")
            if user1_draw_continue == "y":
                user1.append(deal_cards())
            else:
                game_over = True

    while user2_score != 0 and user2_score <17:
        user2.append(deal_cards())
        user2_score = calculate_score(user2)

    print(compare(user1_score,user2_score))

while input("Do you want to play a game of Blackjack? y or n? ") == 'y':
    print("\n"*20)
    play_game()






