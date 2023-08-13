# Dictionaries2.py
# Author: Helen Thomas
# Date: 12.08.2023

colours = {}
colours["red"] = 1
colours["blue"] = 2
colours["green"] = 3

city_population = {"Auckland": 2_500_000,
                   "Wellington": 800_000,
                   "Chrsitchurch": 350_000,
                   "Hamilton": 180_000}

print(city_population)

city_population["Dunedin"] = 87_000

print(city_population)

# join the dictionaires
colours.update(city_population)
print("Joined dictionary:", colours)