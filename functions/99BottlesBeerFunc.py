#  99BottlesBeerFunc.py
#  Author: Helen Thomas
# DAte: 16.08.2023

def bottles_of_beer(num):
    if num == 1:
        return "1 bottle of beer on the wall, 1 bottle of beer.\n"
        "Take it down, pass it around, no more bottles of beer on "
        "the wall.\n"
    elif num == 0:
        return "No more bottles of beer on the wall, no more bottles "
        "of beer.\nGo to the store and buy some more, 99 bottles of "
        "beer on the wall.\n"
    else:
        return "{} bottles of beer on the wall, {} bottles of beer.\nTake one down, pass it around, {} bottles of beer on the wall.\n".format(num, num, num - 1)

for i in range(99, -1, -1):
    verse = bottles_of_beer(i)
    print(verse)
