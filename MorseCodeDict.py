#  MorseCodeDict.py
#  Authr: Helen Thomas
#  Date: 14.08.2023

#  Write a program that takes user input string and converts it to Morse.

morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    " " : "/" # to allow input to contain spaces
}

while True:
    input1 = input("Please write what you want translated into Morse code (type 'exit' to quit).\n")

    # Convert input to uppercase and iterate through characters
    morse_code = ""
    if input1.upper() == 'EXIT':
        exit()  # Exit the program
    for char in input1.upper():
        if char not in morse:
            print("The character '{}' is not supported by this program.".format(char))
            break
        else:
            morse_code += morse[char] + " "  # Add a space after each Morse code

    # Print the Morse code if all characters are supported
    if morse_code:
        print("Morse code:", morse_code)
