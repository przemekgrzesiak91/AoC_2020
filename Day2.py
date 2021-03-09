
data = [line.strip().replace('-',' ').replace(':','').split(' ') for line in open('data/day2.txt')]

def count_good(data):
    counter = 0
    for line in data:
        if line[3].count(line[2]) in range(int(line[0]),int(line[1])+1):
            counter += 1
    return counter

def count_good2(data):
    counter = 0
    for line in data:
        pos1, pos2 = int(line[0]) - 1, int(line[1]) - 1

        if line[3][pos1] != line[3][pos2]:
            if line[3][pos1] == line[2] or line[3][pos2] == line[2]:
                counter += 1
    return counter

print("Day 2.1: ", count_good(data))
print("Day 2.2: ", count_good2(data))