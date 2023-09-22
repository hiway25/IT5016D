# RichterScale.py
#  Autho: Helen Thomas
#  Date: 10.08.2023

#  Elif statement practice

print("Welcome to the Richter Scale helper.")
scale = float(input("Please enter a magnitude value to 1 decimal place. \n"))
print("Thankyou.  The magnitude value you entered is ", scale, "\n")
print("This type of magnitude is considered ", end="")

if scale >= 10.0:
    print("Meteoric")
elif scale >= 8.0:
    print("Great")
elif scale >= 7.0:
    print("Major")
elif scale >= 6.0:
    print("Strong")
elif scale >= 5.0:
    print("Moderate")
elif scale >= 4.0:
    print("Light")
elif scale >= 3.0:
    print("Minor")
elif scale >= 2.0:
    print("Very Minor")
elif scale < 2.0:
    print("Micro")

# Assertion 1; 1.3 will respond "Micro"
# Assertion 2: 11 will respond "Metoric"
# 5.3 will respond "Moderate"

