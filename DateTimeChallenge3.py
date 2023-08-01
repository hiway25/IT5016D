# DateTimeChallenge3.py
# Author: Helen Thomas
# Date: 01.08.23

#Following challenges from course
from datetime import datetime
from datetime import timedelta

date_input1 = input("Please enter your DOB in the format DD Mmm YYYY: \n")
date_input2 = input("Please enter the birthdate of the person you wish to see the age difference for, in the format DD Mmm YYYY: \n")


#cast to a datetime object
date_object1 = datetime.strptime(date_input1, '%d %b %Y')
date_object2 = datetime.strptime(date_input2, '%d %b %Y')

#Challenge one calculation
my_diff = date_object1 - date_object2

print ("The difference in age between the two people is ", my_diff, ".\n")
