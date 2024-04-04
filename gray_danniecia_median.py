'''
Description: This code will  write a program takes in three integers 
and outputs the median value (not the largest or smallest
value).

 
Author: Danniecia
'''
# asks user to enter three numbers 
first_num=int(input("Please enter the first number: "))
second_num=int(input("Please enter the second number: "))
third_num= int(input("Please enter the third number:  "))

#figures out if first number is median and prints if it is 
if (first_num > second_num and first_num < third_num) or (first_num < second_num and first_num > third_num):
    print("The median number is",first_num)

#figures out if second number is median and prints if it is 
elif (second_num > first_num and second_num < third_num) or (second_num < first_num and second_num > third_num):
    print("The median number is",second_num)


#figures out if third number is median and prints if it is
elif (third_num > first_num and third_num < second_num) or (third_num < first_num and third_num > second_num):
    print("The median number is",third_num)