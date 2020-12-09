from itertools import combinations

with open("input.txt", 'r') as f:
    data_stream = f.read()

data_stream = [int(a.strip()) for a in data_stream.split('\n')]

preamble_size = 25

for i in range(preamble_size, len(data_stream)):
    combos = combinations(data_stream[i-preamble_size:i], 2)
    combos = [sum(a) for a in combos]
    
    if data_stream[i] not in combos:
        print("Part 1", data_stream[i])
        invalid_number = data_stream[i]
        break


for i in range(len(data_stream)):
    sum_of_nums = 0
    list_of_nums = []
    for num in data_stream[i:]:
        sum_of_nums += num
        list_of_nums.append(num)
        if sum_of_nums >= invalid_number:
            break
    if sum_of_nums == invalid_number:
        print("Part 2", max(list_of_nums) + min(list_of_nums))
        break
