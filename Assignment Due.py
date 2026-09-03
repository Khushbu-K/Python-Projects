# Assignment Due
# You are eagerly awaiting for the upcoming Technex event organized by IIT BHU Varanasi! However, you also have an assignment due. The deadline for the assignment is in Y days, and it takes you X days to complete it.
# Determine whether you can finish the assignment on or before the deadline.
# Input Format
# The input consists of two space-separated integers X and Y, where:
# 	X denotes the number of days required to complete the assignment.
# 	Y denotes the number of days remaining until the deadline.
# Output Format
# Print YES if you can complete the assignment on or before the due date, otherwise print NO
# You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).
# Constraints
# 	1≤X≤100
# 	1≤Y≤100


# cook your dish here
deadline_day = int(input())
completion_days_required = int(input())

if completion_days_required <= deadline_day:
    print("yes")
else:
    print("no")
