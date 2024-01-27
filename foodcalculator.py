print("Food Price Calculator\n") # Application Name

sales_tax = 0.07 # 7% Sales Tax
restaurant_tip = 0.18 # 18% Tip

# Cost of meal before tax and tip is inputted
meal_price = float(input("Input cost of meal: "))

# This section informs the user what % the tip and tax are
print("Tip is 18% of the total meal's cost\n")
print("Sales tax is 7% of the total meal cost\n")

tip_total = meal_price * restaurant_tip # Calculates the tip
total_tax = meal_price * sales_tax # Calculates the tax
total_meal = meal_price + tip_total + total_tax # Calculates the total meal price with tax and tip included

print("Meal Price:$", meal_price) # Outputs the price of the meal before tax and tip are applied
print("Total Tip:$", tip_total) # Outputs total caclulated tip
print("Sales Tax:$", total_tax) # Outputs total calculated tax
print("Meal Total:$", total_meal) # Outputs the calculated meal total with tax and tip

print("\nBye!")