# Seated Together
# A bus has 100 seats arranged in 20 rows, with 5 seats in each row. Seats 1 to 5 are in the first row, seats 6 to 10 are in the second row, and so on.
# Chef and Chefina are seated in seats X and X+1, respectively.
# They can talk to each other during the journey if and only if both seats are in the same row.
# Given X, determine whether Chef and Chefina will be able to talk to each other.
# Input Format
# 	The input consists of a single integer X, denoting Chef's seat number. Chefina's seat number is hence X+1.
# Output Format
# Output the answer: Yes if it's possible for Chef and Chefina to talk to each other during the journey, and No otherwise.
# Each letter of the output may be printed in either uppercase or lowercase, i.e. the strings NO, No, nO, and no will all be considered equivalent.
# Constraints
# 	1≤X≤99



# cook your dish here
seats = 100
rows = 20
seat_in_rows = seats//rows

x = int(input())
y = x+1
if x%seat_in_rows:
    print("yes")
else:
    print("no")

