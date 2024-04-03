"""
Program Description: This code will write a program that implements a calculator in the terminal. The program will accept an
entire expression as input.


Author:Danniecia Gray
"""
# adds two numbers
def addition(left,right):
    return left + right

#subtracts two numbers
def subtraction(left,right):
    return left - right

#multiplies two numbers
def multiplication(left,right):
    return left * right

#divide two numbers
def division(left,right):
    return left / right

#returns remainder of two numbers divided
def modulus(left,right):
    return left % right

#divides two numbers and rounds to nearest whole number
def floor_division(left,right):
    return left // right

#raises number to the power
def power(left,right):
    return left**right

# calculates the equation entered based on the sign identified 
def calculator(equation):
    left,sign,right=equation.split()
    left,right= float(left),float(right)

    if sign == "+":
        return addition(left,right)

    elif sign == "-":
        return subtraction(left,right)
        
    elif sign == "*":
        return multiplication(left,right)
        
    elif sign == "/":
        return division(left,right)
        
    elif sign == "%":
        return modulus(left,right)
        
    elif sign == "//":
        return floor_division(left,right)
    
    elif sign == "**":
        return power(left,right)
        
    else:
            return("Error: Invalid Operator or Expression!")

        
while True:
    equation=input("Please enter and Expression (space your equation): ")

# stops code if user enters quit, q or Quit
    if equation == "Quit" or equation == "q" or equation == "quit":
        break

# calculates and prints results of equation
    result=calculator(equation)

    print(f"Result: {result}")









