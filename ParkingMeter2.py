# ParkingMeter2.py
# Author: Helen Thomas
# Date: 09.08.2023

#IF ELSE practice

print("Kia ora, this is a parking meter. \n")
park_time = int(input("How long would you like to park today?  \n"))
print("You would like to park for", park_time, " hours. \n")

rate = 4
cost = 0
if park_time > 3:
    cost = rate *3
    #drop the rate by $2
    rate -= 2
    #get the remainder of the parking time
    park_time -= 3
    # add to the current cost
    cost += rate * park_time
    print("The cost of the parking is $", cost)
else:
    cost = rate * park_time
    print("The cost of parking is $", cost)


#test case assertion 1
'''
park_time = 4
total cost of parking = $14
'''

#test case assertion 2
'''
park_time = 10
total cost of parking = $26'''

#test case assertion 3
'''
park_time = 20
total cost of parking = $46'''