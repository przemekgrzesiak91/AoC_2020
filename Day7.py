data = [line.strip().split(' bags contain ') for line in open('data/day7.txt','r')]

bags_dict = {}

# Create bags dictionary
for line in data:
    value = line[1]
    if value == 'no other bags.': value = 'none'
    bags_dict[line[0]] = value.split(',')

valid_bags = ['shiny gold']

for bag in valid_bags:
    for key, values in bags_dict.items():
        for value in values:
            bag_color = ' '.join(value.split()[1:3])
            if bag_color == bag  and key not in valid_bags:
                valid_bags.append(key)

print("Day 7.1: ", len(valid_bags)-1)

in_shiny = bags_dict['shiny gold']
n_bags = 0

for bag in in_shiny:
    value, name = int(bag.split()[0]), ' '.join(bag.split()[1:3])
    n_bags += value

    for i in range(len(bags_dict[name])):
        if bags_dict[name][i] == 'none':
            continue
        else:
            value_inside, name_inside = int(bags_dict[name][i].split()[0]), ' '.join(bags_dict[name][i].split()[1:3])
            value_inside *= value
            new_value = str(value_inside) + ' ' + name_inside
            in_shiny.append(new_value)

print("Day 7.2: ", n_bags)