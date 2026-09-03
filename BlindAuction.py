# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)


def my_auction(bidding_dictionary):
    winner = ""
    highest_bid = 0
    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amt = bidding_dictionary[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder

    print(f"The winner is {winner} with a bid of {bid_amt}")

bids={}
continue_bidding = True
while continue_bidding:
    name = input("Whats your name? ")
    bid_amt = float(input("Whats the amount you like to bid? "))
    bids[name] = bid_amt
    more_bidder=input("Is there anyone who would like to bid? y or n? ")
    if more_bidder == "n":
        continue_bidding = False
        my_auction(bids)
    elif more_bidder == "y":
        print("\n" * 5)


