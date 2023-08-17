#  SplittingJoiningStrings.py
# Author: Helen Thomas
# Date: 18.08.2023

problems = 'broke, pale, short, nerdy'
print(problems)

l = problems.split(", ")

print(l)

joined = ' and '.join(l)
print(joined)

csv = ','.join(l)
print(csv)