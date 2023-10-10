with open("input.txt", 'r') as f:
    strings = f.readlines()

vowels = ['a', 'e', 'i', 'o', 'u']

forbidden = ['ab', 'cd', 'pq', 'xy']

nice = []

def a(string):
    for i in range(0,len(string)-1):
        if string[i] == string[i+1]:
            return True

def b(string):
    total = 0
    for vowel in vowels:
        total += string.count(vowel)
    if total >= 3:
        return True

def c(string):
    total = 0
    for case in forbidden:
        total += string.count(case)
    if total == 0:
        return True

def d(string):
    for i in range(0,len(string)-2):
        if string[i] == string[i+2]:
            return True

def e(string):
    for i in range(0,len(string)-1):
        if string.count(string[i:i+2]) >= 2 and string[i:i+3] != string[i]*3:
            return True
    
for string in strings:
    if (a(string), b(string), c(string)) == (True, True, True):
        nice.append(string)

print("Part One:", len(nice))

new_nice = []

for string in strings:

    if (d(string), e(string)) == (True, True):
        new_nice.append(string)

print("Part Two:", len(new_nice))