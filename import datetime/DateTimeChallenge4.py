# DateTimeChallenge4.py
# Author: Helen Thomas
# Date: 08.08.23

from datetime import datetime
from datetime import timedelta

date_input = input("Please enter a date in DD Mmm YYYY format: \n")

year_add = int(input("Please enter a  whole number of years to add to the date entered: \n"))

#Cast to datetime object
date_object = datetime.strptime(date_input, '%d %b %Y')

#calculations
new_date = date_object + timedelta(days = year_add*365)

print ("The date after",year_add, "years is" ,new_date)
