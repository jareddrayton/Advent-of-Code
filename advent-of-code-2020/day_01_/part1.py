import itertools

with open('input.txt', 'r') as f:
    nums = f.readlines()

nums = [int(n) for n in nums]

for a, b in itertools.combinations(nums, 2):
    if a + b == 2020:
        print(a*b)
        break

for a, b, c in itertools.combinations(nums, 3):
    if a + b + c == 2020:
        print(a*b*c)
        break

def general(numbers, r, total):
    for combination in itertools.combinations(numbers, r):
        if sum(combination) == total:
            print()
