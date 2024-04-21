"""
Description: This code will write a program that reads the number of steps from a user, calls the steps_to_miles() function, and
outputs the returned value from the steps_to_miles() function.It will use a try-except block to catch any
ValueError, or NegativeValueError object raised by the steps_to_miles() function and output the
exception message.It will output each floating-point value with two digits after the decimal point, which can
be achieved as follows:

print(f'{your_value:.2f}')

Author:Danniecia Gray
"""

class NegativeValueError(Exception):
    def __init__(self,error="Exception: Negative Step Count Entered"):
        self.error = error

def steps_to_miles(num_steps):
    try:
        steps = int(num_steps)
        if steps  < 0:
            raise NegativeValueError()
        
        miles = steps/2000
        return miles
    
    except ValueError:
        raise ValueError("Exception: Non-Numeric Value Entered")

try:
    user_steps = input("Enter the number of steps: ")
    user_miles = steps_to_miles(user_steps)

    print(f"{user_miles:.2f} miles")

except(ValueError, NegativeValueError) as excpt:
    print(excpt)
    




