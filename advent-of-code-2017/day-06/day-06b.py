import itertools

with open("day-06-input.txt", 'r') as f:
    memorybanks = f.readline().split()

memorybanks = list(map(int, memorybanks))

states = []

current_state = memorybanks
    
counter_a = 0

while states.count(current_state) < 1:
    states.append(memorybanks)
    biggest_block = max(memorybanks)
    biggest_block_location = memorybanks.index(biggest_block)

    memorybanks = memorybanks[biggest_block_location+1:] + memorybanks[:biggest_block_location+1]

    memorybanks[len(memorybanks)-1] = 0

    A, B = divmod(biggest_block, len(memorybanks))
    
    new = [A for i in range(0, len(memorybanks))]
    new2 = [1 if i < B else 0 for i in range(0, len(memorybanks))]
    new3 = [x + y for x, y in zip(new, new2)]

    memorybanks = [x + y for x, y in zip(new3, memorybanks)]
    memorybanks = memorybanks[len(memorybanks) - biggest_block_location-1:] + memorybanks[:len(memorybanks)-biggest_block_location-1]

    current_state = memorybanks

    counter_a +=1



with open("day-06-input.txt", 'r') as f:
    memorybanks = f.readline().split()

memorybanks = list(map(int, memorybanks))

states = []

current_state = memorybanks
    
counter_b = 0

while states.count(current_state) < 2:
    states.append(memorybanks)
    biggest_block = max(memorybanks)
    biggest_block_location = memorybanks.index(biggest_block)

    memorybanks = memorybanks[biggest_block_location+1:] + memorybanks[:biggest_block_location+1]

    memorybanks[len(memorybanks)-1] = 0

    A, B = divmod(biggest_block, len(memorybanks))
    
    new = [A for i in range(0, len(memorybanks))]
    new2 = [1 if i < B else 0 for i in range(0, len(memorybanks))]
    new3 = [x + y for x, y in zip(new, new2)]

    memorybanks = [x + y for x, y in zip(new3, memorybanks)]
    memorybanks = memorybanks[len(memorybanks) - biggest_block_location-1:] + memorybanks[:len(memorybanks)-biggest_block_location-1]

    current_state = memorybanks

    counter_b +=1

# 1h59m06s
print("Part Two:", counter_b - counter_a)