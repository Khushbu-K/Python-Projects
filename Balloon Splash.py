# Balloon Splash
# Alice and Bob are playing a balloon splash game.
# Alice has X water balloons and Bob has Y water balloons.
# The player with more balloons wins. If both players have the same number of balloons, the result is a draw.
# Output:
# 	Alice if Alice wins
# 	Bob if Bob wins
# 	Draw if it is a draw
# Input Format
# 	The first line contains two space-separated integers X and Y.
# Output Format
# Output a single string denoting the result of game:
# 	Alice if Alice wins
# 	Bob if Bob wins
# 	Draw if it is a draw
# Each character can be printed in either uppercase or lowercase, i.e. if the winner is Bob, the outputs BOB, Bob, bOb, and so on will all be accepted.
# Constraints
# 	1≤X,Y≤100


# cook your dish here
(x, y) = map(int, input().split())

total_balloon = x + y

for i in range(total_balloon):
    if x > y:
        print("Alice")
    elif x == y:
        print("Draw")
    else:
        print("Bob")

