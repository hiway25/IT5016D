#  AreaAndVolumeWhileLoop.py
#  Author: Helen Thomas
#  Date: 10.08.2023

#  calculate the area of the shape shown
#  calculate the volume of the shape shown
#  exit the program


print("Welcome to our area and volume calculator.")

while True:
    choice = input("Would you like to calculate the (a) Area or (b) Volume of the shape? Type 'exit' to leave the program.\n")
    if choice.lower() == "exit":
        print("Exiting the program.")
        break  # Exit the loop if the user types 'exit'
    elif choice.lower() == "a" or choice.lower() == "b":
        x = int(input("Please enter the value of x: "))
        y = int(input("Please enter the value of y: "))
        if 0 < x <= 10 and 0 < y <= 8:
            if choice.lower() == "a":
                total_area = (10 * 8) - (x * y)
                print("The area of your shape is", total_area, "cm2\n")
            else:
                total_area = (10 * 8) - (x * y)  # Ensure we have the latest total_area
                total_volume = total_area * 3
                print("The volume of your shape is", total_volume, "cm3\n")
        else:
            print("Invalid input. x should be between 1 and 10, and y should be between 1 and 8.")
    else:
        print("Invalid choice. Please enter 'a', 'b', or 'exit'.")


'''
Test assertion 1 ; a, 2, 2, = 76cm2
Test assertion 2; a, 11, 5, = Error message
Test assertion 3; b, 5, 5 = 165cm3
'''













