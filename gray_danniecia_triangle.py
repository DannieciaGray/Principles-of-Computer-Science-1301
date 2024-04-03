'''
Description: This code will write a program that calculates several properties of a triangle. Using the user-entered side lengths, 
the program will output the answers to the following questions:

1.	What is the perimeter of the triangle?
2.	What is the area of the triangle?
3.	Is the triangle an acute, obtuse, or right triangle?

Author: Danniecia
'''
#imports math operators 
import math

#asks the user to input the length of sides A,B,and C
length_A = int(input("Please enter the length of side A of the Triangle (in meters):"))
length_B = int(input("Please enter the length of side B of the Triangle (in meters):"))
length_C = int(input("Please enter the length of side C of the Triangle (in meters):"))

#calculates the perimeter of triangle
perimeter =length_A + length_B + length_C

#calculates the semi-perimeter of triangle
semi_peri=1/2*(perimeter)

#calculates the area of triangle
area = math.sqrt(semi_peri*(semi_peri-length_A)*(semi_peri-length_B)*(semi_peri-length_C))

#Prints perimeter of triangle
print("The perimeter of the triangle is",perimeter,"m")

#Prints area of triangle
print(f"The area of the triangle is {area:,.2f} m^2")


# Returns the type of triangle based on the use of Pythagorean Theorem (a^2+b^2=c^2)

if (length_A**2)+(length_B**2)==(length_C**2): #Right Triange if a^2+b^2=c^2

    print("It is a Right Triangle.")

elif(length_A**2)+(length_B**2)>(length_C**2): #AcuateTriange if a^2+b^2>c^2

    print("It is an Acute Triangle")

elif(length_A**2)+(length_B**2)<(length_C**2): #Obtuse Triange if a^2+b^2<c^2

    print("It is an Obtuse Triangle")
