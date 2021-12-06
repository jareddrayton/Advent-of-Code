with open("day-04-input.txt", 'r') as f:
    entries = f.readlines()


entries.sort()

print(entries)

guards = {}

for entry in entries:
    print(entry.strip())

print(entries[0])
print(entries[-1])

for entry in entries:
    entry = entry.strip().split("] ")
    
