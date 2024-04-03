'''
Description: This code will write a program that simulates a point-of-sale device for a
restaurant.The program will store the menu items and their prices as a dictionary. Users will be
prompted for the quantity of each item on the menu. The program will then calculate the total cost of
the order.

Author: Danniecia
'''

#adds menu items to dictionary
menu={"Hot Dog":1.50,"Slice of Pizza":1.99,"Whole Pizza":9.95,"Soft Drink":0.59}


#asks user to input number of menu items they want 
num_hotdog=int(input("Please enter the number of Hot Dogs:"))
num_slices=int(input("Please enter the number of Pizza Slices:"))
num_pizza=int(input("Please enter the number of Whole Pizzas:"))
num_drinks=int(input("Please enter the number of Soft Drinks:"))

#calculates the cost of each menu item user requested 
hot_dog= menu["Hot Dog"]*num_hotdog
pizza_slices= menu["Slice of Pizza"]*num_slices
whole_pizza=menu["Whole Pizza"]*num_pizza
soft_drink=menu["Soft Drink"]*num_drinks

#calculates total
total=hot_dog+pizza_slices+whole_pizza+soft_drink

#prints total
print(f"The total cost of the order is $ {total:,.2f}")