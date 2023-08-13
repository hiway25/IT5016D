# Tuple.py
#  Author: Helen Thomas
#  Date: 12.08.2023

bank_accounts = (("Joe", 33, "234 Great South Road", "022629107"),
                 ("Tama", 6000),
                 ("Suzanne", 21025, "45 Green Lane"),
                 ("Anihera", -75))

print("The number of bank accounts is ", len(bank_accounts))

# showing names and balances
for i in bank_accounts:
    print("\nThe name is ", i[0], " and the balance is $", i[1])

# showing only names with addresses
for i in bank_accounts:
    if len(i) > 2:
        print("\nThe name is ", i[0], " and the address is ", i[2])

# showing only the names of people with <$100
for i in bank_accounts:
    if i[1] < 100:
        print (i[0])

# The names of customers with no address and no phone number
for i in bank_accounts:
    if len(i) < 3:
        print("\n", i[0], " has no phone or address information")

# the highest and lowest balances
balances = [account[1] for account in bank_accounts]
highest_balance = max(balances)
lowest_balance = min(balances)
print("The highest balance is: $", highest_balance,"and the lowest balance is: $", lowest_balance)

# the sum of the balances
total_balance = sum(balances)
print("The sum of the balances is $", total_balance)


print("The number of bank accounts is", len(bank_accounts))

# Print full details for all customers
print("\nAll customer details:")
for customer in bank_accounts:
    print("Name:", customer[0])
    print("Balance: $", customer[1])
    if len(customer) > 2:
        print("Address:", customer[2])
    if len(customer) > 3:
        print("Phone:", customer[3])
    print("")

# Print full details for customers with more than $5000 or customers who are overdrawn
print("Customer details for customers with more than $5000 or overdrawn:")
for customer in bank_accounts:
    if customer[1] > 5000 or customer[1] < 0:
        print("Name:", customer[0])
        print("Balance: $", customer[1])
        if len(customer) > 2:
            print("Address:", customer[2])
        if len(customer) > 3:
            print("Phone:", customer[3])
        print("")
