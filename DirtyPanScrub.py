# DirtyPanScrub.py
#  Author: Helen Thomas
#  Date: 10.08.2023

import random
dirty = True
scrub_count = 0

while(dirty):

    scrub_count += 1
    print("Scrub the pan: {}".format(scrub_count))
    print('Rinse & check if the pan is clean.')

    if not random.randint(0, 9):
        print("All clean")
        dirty = False
    else:
        print("Still dirty")