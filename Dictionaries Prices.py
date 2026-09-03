# Create a new dictionary called Price_list that contains the first five meals 
# of the Menu dictionary as keys and assign the following five values as 
# prices (assumed in dollars): 10, 5, 8, 12, 5. Start by Price_list = {}.


Menu = {'meal_1':'Spaghetti', 'meal_2':'Fries', 'meal_3':'Cheeseburger', 'meal_4':'Lasagna', 'meal_5':'Soup'}
Price_list = {}

prices = [10,5,8,12,5]

for i in range(1,6):
    key = f"meal_{i}"
    Price_list[Menu[key]] = prices[i-1]

print(Price_list)
    


