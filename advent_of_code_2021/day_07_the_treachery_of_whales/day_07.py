from functools import cache

with open('input.txt', 'r') as f:
    crab_positions = list(map(int, f.readline().strip().split(',')))

@cache
def sum_range(n):
    return sum(range(1, n+1))

def new_function(crab_positions, extra_expense):
    min_, max_ = min(crab_positions), max(crab_positions)
    
    fuel_list = []
    
    for i in range(min_, max_):
        fuel = 0
        for position in crab_positions:
            if not extra_expense:
                fuel += abs(position - i)
            else:
                fuel += sum_range(abs(position - i))
        fuel_list.append(fuel)

    return min(fuel_list)

print('Part 1:', new_function(crab_positions, False))
print('Part 2:', new_function(crab_positions, True))
