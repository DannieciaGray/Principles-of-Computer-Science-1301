"""
Description: This code will write a program that implements multiple objects of the Number class.
The program will demonstratethe functionality of all 5 specified Operators.

Author:Danniecia Gray
"""

#number class 
class Number:
    def __init__(self,num=25):
        self.num=num

    def __str__(self):
        #return string 
        return(str(self.num))

    def __add__(self,other):
        #return add
        return self.num + other

    def __sub__(self,other):
        #return subtraction
        return self.num - other
    
    def __mul__(self,other):
        #return multiplication
        return self.num * other
    
    def __truediv__(self,other):
        #return division 
        return self.num // other


#makes the class a variable
number= Number()

#asks the user to input a number
user_num= int(input("Enter a number: "))


#prints each equation and its results
print(number.__str__())
print(f"{number.__str__()} + {user_num} = {number.__add__(user_num)}")
print(f"{number.__str__()} - {user_num} = {number.__sub__(user_num)}")
print(f"{number.__str__()} * {user_num} = {number.__mul__(user_num)}")
print(f"{number.__str__()} / {user_num} = {number.__truediv__(user_num)}")

print(f"({number.__add__(user_num)} + {number.__sub__(user_num)} * {number.__truediv__(user_num)} ) / {number.__mul__(user_num)} \
= {(number.__add__(user_num) + number.__sub__(user_num) * number.__truediv__(user_num)) // number.__mul__(user_num) }")

