# You buy N cakes from Chef's bakery. Normally, each cake costs 100 rupees.
# However, Chef has a special discount offer. If you buy at least 5 cakes, then you get a 15 percent discount on all your bought cakes, i.e. each cake costs only 85 rupees.
# Find the cost, in rupees, that you paid for the N cakes.
# Input Format
# 	The first and only line contains 1 integer N.
# Output Format
# Output the cost of buying N cakes.
# Constraints
# 	1≤N≤10


# cook your dish here
cake_cost = 100
number_of_cakes = int(input())

total_cost = 0
if number_of_cakes >= 5:
    total_cost = number_of_cakes * cake_cost
    total_cost = total_cost - ((total_cost * 15)/100)
    print(f"The total cost of {number_of_cakes} cake is {total_cost}.")
else:
    total_cost = cake_cost * number_of_cakes
    print(f"The total cost of {number_of_cakes} cake is {total_cost}.")
