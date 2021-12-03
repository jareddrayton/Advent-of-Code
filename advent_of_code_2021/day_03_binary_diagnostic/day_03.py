with open('input.txt', 'r') as f:
    diagnostic_report = [list(line.strip()) for line in f.readlines()]

gamma_rate, epsilon_rate = [], []

for position in zip(*diagnostic_report):
    if position.count('1') > position.count('0'):
        gamma_rate += '1'
        epsilon_rate += '0'
    elif position.count('1') < position.count('0'):
        gamma_rate += '0'
        epsilon_rate += '1'

gamma_rate = int(''.join(gamma_rate), 2)
epsilon_rate = int(''.join(epsilon_rate), 2)

print(gamma_rate * epsilon_rate)


def get_rating(diagnostic_report, n, rating_type):

    if len(diagnostic_report) == 1:
        return int("".join(diagnostic_report[0]), 2)

    if rating_type == 'co2':
        i, j = '0', '1'
    elif rating_type == 'oxygen':
        i, j = '1', '0'

    pos_numbers = list(zip(*diagnostic_report))[n]

    sum_0, sum_1 = pos_numbers.count('0'), pos_numbers.count('1')

    if sum_0 > sum_1:
        diagnostic_report = [y for x, y in zip(pos_numbers, diagnostic_report) if x == i]
    elif sum_0 <= sum_1:
        diagnostic_report = [y for x, y in zip(pos_numbers, diagnostic_report) if x == j]

    n += 1

    return get_rating(diagnostic_report, n, rating_type)

CO2_scrubber_rating = get_rating(diagnostic_report, 0, 'co2')
oxygen_generator_rating = get_rating(diagnostic_report, 0, 'oxygen')

life_support_rating = CO2_scrubber_rating * oxygen_generator_rating

print(life_support_rating)