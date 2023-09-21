# Divisible7.py
# Author: Helen Thomas
# Date: 11.08.2023

n1=[]
for x in range (1500, 2701):
    if (x % 7 == 0) and (x % 5 ==0):
        n1.append(str(x))
print(','.join(n1))
