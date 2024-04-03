"""
Description: This code will write a program that implements an object of the VendingMachine class. The 
program will allow the user to enter multiple commands as input until a stop word is detected. 

Author:Danniecia Gray
"""

# Creating class for vending machine, returns inventory and purchased amount
class VendingMachine:
    def __init__(self,num_soda=10,num_water=10,num_coffee=10):
        self.soda   =  num_soda
        self.water  =  num_water
        self.coffee = num_coffee

    #returns the amount of items in inventory 
    def inventory(self):
        
        return f'Soda:{self.soda}\nWater:{self.water}\nCoffee:{self.coffee}'
    
    #calculates and returns the amount purchased
    def purchase(self, option, amount):
        if option == "1":
            if self.soda >= amount:
                self.soda -= amount
                return f"Purchased:{amount}"
            
            else:
                return "Soda Inventory Needs Restock"
        
        elif option == "2":
            if self.coffee  >= amount:
                self.coffee -= amount
                return f"Purchased: {amount}"
            
            else:
                return "Coffee Inventory Needs Restock"
            
        elif option == "3":
            if self.water >= amount:
                self.water -= amount
                return f"Purchased: {amount}"
            
            else:
                return "Water Inventory Needs Restock"
            
        else:
            return "Invalid Option."

            
vending_machine = VendingMachine()  

# asks the user to pick an item unless they enter quit (code stops if user enters quit)
while True:
    drink_option=(input("1 - Soda\n2 - Coffee\n3 - Water\nPlease select an option:"))
    if drink_option.lower() == "quit":
        break
        
    amount= int(input("Please enter an amount:"))


    print(vending_machine.purchase(drink_option,amount))
    print(vending_machine.inventory())

