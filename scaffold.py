import os

year = "2018"

for i in range(1,26):
    os.makedirs("advent-of-code-{}\\day-{:02d}".format(year, i))