import os

year = "2017"

for i in range(1,26):
    os.makedirs("advent-of-code-{}\\day-{:02d}".format(year, i))