import re

data = [line.replace('\n',' ').split()  for line in open('data/day4.txt','r').read().split('\n\n')]
passports  = [dict(tuple(field.split(':')) for field in line) for line in data]


valid_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
ecl_color = 'amb blu brn gry grn hzl oth'.split()
hcl_pattern = re.compile("^[a-f0-9]+$")

valid_passports = []
for passport in passports:
    if all(field in passport.keys() for field in valid_fields):
        valid_passports.append(passport)

# 4.2
n_valid_passport = 0
for passport in valid_passports:
    n_valid_value = 0
    for key, value in passport.items():
        if key == 'byr' and 1920 <= int(value) <= 2002: n_valid_value += 1
        if key == 'iyr' and 2010 <= int(value) <= 2020: n_valid_value += 1
        if key == 'eyr' and 2020 <= int(value) <= 2030: n_valid_value += 1
        if key == 'hgt':
            if value[-2:] == 'cm' and len(value) == 5 and (150 <= int(value[0:3]) <= 193)\
                    or value[-2:] == 'in' and len(value) == 4 and (59 <= int(value[0:2]) <= 76) : n_valid_value += 1
        if key == 'hcl' and value[0] == '#' and bool(hcl_pattern.match(value[1:])): n_valid_value += 1
        if key == 'ecl' and value in ecl_color: n_valid_value += 1
        if key == 'pid' and len(value) == 9: n_valid_value += 1
    
    if n_valid_value == 7:
        n_valid_passport += 1

print("Day 4.1: ", len(valid_passports))
print("Day 4.2: ",n_valid_passport)
