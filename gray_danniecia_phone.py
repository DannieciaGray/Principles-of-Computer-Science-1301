'''
Description: This code will  write a program that formats a given phone number
as input. Given an integer representing a 10-digit phone number, output the area code, prefix, and line
number using the format (800) 555-1212.
 

Author: Danniecia
'''

#Asks the user to enter their phone number 
phone_num= int(input("Please enter your phone number:"))

#separates the area code from the rest of the phone number
area_code=phone_num//10000000

#separates the first three digits from the rest of the phone number
first_digits=(phone_num//10000)%1000

#separates the last four digits from the rest of the phone number
last_digits=phone_num%10000

#prints the phone number using the format (000) 000-0000
print("Phone Number:","(",area_code,")",first_digits,"-",last_digits)