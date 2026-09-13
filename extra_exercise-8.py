# Creating a menu
# Use print statement to create a menu that displays a numbered list of options.
# Then prompt for user to choose an option.
# Use if statement to print a different message for each option in the menu.
print("1. Pizza")
print("2. Fried Chicken")
print("3. Drinks")
print("4. Salad")
user_option = input("Choose an option: ")
if user_option == "1":
    print("There are Cheese pizza, BBQ Chicken pizza and Hawaiian pizza. ")
elif user_option == "2":
    print("There are lemon fried chicken, garlic fried chicken and honey garlic fried chicken.")
elif user_option == "3":
    print("There are Coca-Cola, Pepsi and Coffee.")
elif user_option == "4":
    print("There are Greek Salad, Garden Salad and Caesar Salad.")
else:
    print("The menu you want is not listed in the shop.")