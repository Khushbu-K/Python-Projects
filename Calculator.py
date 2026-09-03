import art
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

calc_dictionary = {"+":add,
                   "-":subtract,
                   "*":multiply,
                   "/":divide}

def my_calculator():
    print(art.logo)
    should_continue = True
    num1 = float(input("Type the first number: \n"))  # \n for taking input in new line

    while should_continue:
        for symbol in calc_dictionary:
            print(symbol)
        operator_sel = input(f"Type the operation: \n")
        num2 = float(input("Enter 2nd number: "))
        final_Result = calc_dictionary[operator_sel](num1, num2)
        print(f"{num1} {operator_sel} {num2} = {final_Result}")

        should_continue = input("Do you want to continue? y/n? ")
        if should_continue == "y":
            num1 = final_Result
            continue
        else:
            print("")
            should_continue = False
            my_calculator()

my_calculator()

