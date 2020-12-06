import re

with open('input.txt', 'r') as f:
    passports = f.read()

passports = passports.replace(' ','\n' )
passports = passports.split('\n')
passports = [passport if passport != "" else "-" for passport in passports]
passports = " ".join(passports)
passports = passports.split("-")

valid = 0

for passport in passports:
    if passport.count(":") == 8 or (passport.count("cid") == 0 and passport.count(":") == 7):
        valid += 1
print("Part 1", valid) 

def part_two(passports):
    
    passports = [passport.strip().split(' ') for passport in passports]
    passports = [[a.split(':') for a in passport] for passport in passports]
    passports = [{k:v for k, v in passport} for passport in passports]
    validated_passports = 0    

    for passport in passports:
        passport.pop('cid', None)
        if len(passport.keys()) == 7:
            validate_passport(passport)
            if all([v[1] for k, v in passport.items()]):
                #print(passport)
                validated_passports += 1
    
    return validated_passports


def validate_passport(passport):

    passport['byr'] = (passport['byr'], 1920 <= int(passport['byr']) <= 2002)
    
    passport['iyr'] = (passport['iyr'], 2010 <= int(passport['iyr']) <= 2020)
    
    passport['eyr'] = (passport['eyr'], 2020 <= int(passport['eyr']) <= 2030)
    
    if passport['hgt'].count('in') > 0 and passport['hgt'].count('cm') > 0:
        passport['hgt'] = (passport['hgt'], False)
        print(passport['hgt'])
    
    elif passport['hgt'].count('in') > 0  :
        passport['hgt'] = (passport['hgt'], 59 <= int(passport['hgt'].strip('in')) <= 76)
    
    elif passport['hgt'].count('cm') > 0:
        passport['hgt'] = (passport['hgt'], 150 <= int(passport['hgt'].strip('cm')) <= 193)

    else:
        passport['hgt'] = (passport['hgt'], False)


    if re.search(r'^#[\da-f]{6}', passport['hcl']):
        passport['hcl'] = (passport['hcl'], True)
    else:
        passport['hcl'] = (passport['hcl'], False)
    
    if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        passport['ecl'] = (passport['ecl'], True)
    else:
        passport['ecl'] = (passport['ecl'], False)

    if re.search(r'[\d]{9}', passport['pid']) and len(passport['pid']) == 9:
        passport['pid'] = (passport['pid'], True)
    else:
        passport['pid'] = (passport['pid'], False)
    

    




print("Part 2", part_two(passports))

