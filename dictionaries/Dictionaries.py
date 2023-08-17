# Dictionaries.py
# Author: Helen Thomas
# Date: 12.08.2023

d = {}
d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 16

print(d["George"])
print(d["Tom"])
print(d["Jenny"])

d["Jenny"] = 20
print(d["Jenny"])

# keys are commonly strings or numbers
d[10] = 100
print(d[10])

# how to iterate over key-value pairs?
for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print("")
