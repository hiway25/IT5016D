# DateTimeChallenge1.py
# Author: Helen Thomas
# Date: 01.08.23

#Following challenges from course
from datetime import datetime
from datetime import timedelta

date_input = input("Please enter a date of your choice in the format DD Mmm YYYY: \n")

#cast to a datetime object
date_object = datetime.strptime(date_input, '%d %b %Y')

#Challenge one calculation
my_125 = date_object - timedelta(days=125)

print ("125 days ago, the date was ", my_125, ".\n")
