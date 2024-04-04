'''
Description: This code will  write a program that when given a highway number, 
indicate whether it is a primary, auxiliary highway or an invalid highway
number. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs
north/south or east/west.

 
Author: Danniecia
'''
#creates list ranging from 1,99
primary_interstate=list(range(1,100))

#asks user to input an interstate number
interstate_num=int(input("Please enter an interstate number: "))

#if number ranges from 1-99 it's a primary highway
if interstate_num>=1 and interstate_num<=99:

    #even number=east/west
    if interstate_num%2==0:
        print("I-",interstate_num,"is primary, going east/west")

    #odd number = north/south
    else:
        print("I-",interstate_num,"is primary, going north/south")

#if number ranges from 100-999 it's an auxiliary highway
elif interstate_num>=100 and interstate_num<=999:

    #if last two digits are 00 then the number isn't valid
    if interstate_num%100==00:
       print(interstate_num,"is not a valid interstate number")

    #if last two digits are in the primary interstate list conduct one of the two statements below 
    if (interstate_num%100 in primary_interstate): 
       
       #last two digits even= east/west and print the primary highway it's serving
       if (interstate_num%100)%2==0:
        print("I-",interstate_num,"serving I-",interstate_num%100,"going east/west")

      #last two digits odd= north/south and print the primary highway it's serving
       else:
        print("I-",interstate_num,"serving I-",interstate_num%100,"going north/south")
       

    
    