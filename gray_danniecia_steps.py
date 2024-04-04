'''
Description: This code will define a function named feet_to_steps() that takes
a float as a parameter, representing the number of feet walked, and returns an integer that represents
the number of steps walked. Then, write a main program that reads the distanced walked in feet as an
input, calls function feet_to_steps() with the input as an argument, and outputs the number of steps as
an integer.

Author: Danniecia
'''
# function converts feet to steps 
def feet_to_steps(feet):
    step=2.5
    feet=int(feet/step)
    return feet

# main program that reads the distance walked in feet as an input and calls the function
distance_travelled=float(input("Please enter the distance travelled in feet: "))

#outputs the number of steps as an integer
print(feet_to_steps(distance_travelled),"steps")


