'''
Description: This code will  write a program that is given two integers representing a speed limit and driving speed in miles per hour
(mph) and outputs the traffic ticket amount.
 

Author: Danniecia
'''

# asks the user to enter vehicle speed and speed limit (only accepts integers)
speed_lim=int(input(("Please enter the speed limit for the road: ")))
vehicle_speed=int(input(("Please enter the vehicle's recorded speed: ")))


#if Driving 10 mph under the speed limit (or slower) receives a $50 ticket.
if vehicle_speed<=speed_lim-10:

    print("The fine is $50")


#else if Driving 6 - 20 mph over the speed limit receives a $75 ticket.
elif vehicle_speed>=speed_lim+6 and vehicle_speed<=speed_lim+20:

    print("The speeding fine is $75")


#else if Driving 21 - 40 mph over the speed limit receives a $150 ticket.
elif vehicle_speed>=speed_lim+21 and vehicle_speed<=speed_lim+40:
    print("The speeding fine is $150")


#else if Driving faster than 40 mph over the speed limit receives a $300 ticket
elif vehicle_speed>speed_lim+40:
    print("The speeding fine is $300")


#else, no ticket is received.
else:
    print("There is no fine")

