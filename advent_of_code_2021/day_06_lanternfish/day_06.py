with open('input.txt', 'r') as f:
    lanternfish = list(map(int, f.readline().strip().split(',')))

def calculate_fish(lantern_fish, days):
    lantern_fish = [lantern_fish.count(i) for i in range(8, -1, -1)]

    for _ in range(days):
        lantern_fish = lantern_fish[-1:] + lantern_fish[:-1]
        lantern_fish[2] += lantern_fish[0]
    return sum(lantern_fish)

print('Part 1:', calculate_fish(lanternfish, 80))
print('Part 2:', calculate_fish(lanternfish, 256))
