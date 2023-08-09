#  SoundLevels.py
#  Author: Helen Thomas
#  Date: 10.08.2023

#  Practicing elif statements including when a value falls between two defined values

print("Welcome to the Sound Decibel identifier.")
decibels = int(input("Please enter a decibel level \n"))
print("Thankyou.  The decibel level you entered is ", decibels, "\n")
print("This type of decibel is ", end="")

if decibels > 130:
    print("higher than our table can go.")
elif decibels == 130:
    print("a Jackhammer")
elif decibels < 130 and decibels > 106:
    print("between a Petrol Lawnmower and a Jackhammer")
elif decibels == 106:
    print("a Petrol Lawnmower")
elif decibels < 106 and decibels > 70:
    print("between an Alarm Clock and a Petrol Lawnmower")
elif decibels == 70:
    print("an Alarm Clock")
elif decibels < 70 and decibels >40:
    print("between a quiet room and an Alarm Clock")
elif decibels == 40:
    print("a Quiet Room")
else: print("quieter than our table can go")

# Test assertions: input 125; output "Between petrol lawnmower and Jackhammer
# Test assertions 2: input 150; output; Higher than our table can go
#  Test assertion 3: 23; output: quiet than our tabl can go