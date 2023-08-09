# CellPhoneBill.py
# Author: Helen Thomas
# Date: 09.08.2023


base_minutes = 50
base_message = 50
base_cost = 15.00
additional_minute_cost = 0.25
additional_message_cost = 0.15
flat_fee = 0.44
tax_rate = 0.05

#Get user input for text and phone calls

txt_used = int(input("Please enter the number of text messages sent this month."))
calls_used = int(input("Please enter the number of call minutes used this month"))

# Calculate additional charges
additional_minute_cost = round(max(calls_used - base_minutes, 0) * additional_minute_cost)
additional_message_cost = round(max(txt_used - base_message, 0) * additional_message_cost)

#  Calculate subtotal
subtotal = base_cost + additional_message_cost + additional_minute_cost + flat_fee

# calculate tax
tax = round(subtotal * tax_rate)

#  calculate total bill
total_bill = round(subtotal + tax)

#Display charges and total bill

print("Cell Phone Bill Details:")
print("Base charge:  $", base_cost)
if additional_minute_cost >0:
    print("Additional minutes charge:  $",additional_minute_cost,)
if additional_message_cost >0:
    print("Additional message charge:  $", additional_message_cost)
print("Flat Fee for 111 service:  $", flat_fee)
print("Tax:  $", tax,)
print("Total Bill amount:  $", total_bill, )