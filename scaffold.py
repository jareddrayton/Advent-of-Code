import os

year = '2021'

for i in range(1, 26):
    os.makedirs(os.path.join(f'advent_of_code_{year}', 'day_{:02d}'.format(i)))
