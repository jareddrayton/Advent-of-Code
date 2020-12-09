import os

year = "2020"

for i in range(1,26):
    os.makedirs("advent_of_code_{}\\day_{:02d}".format(year, i))