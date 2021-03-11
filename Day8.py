import copy
data = [list(line.strip().split(' ')) for line in open('data/day8.txt')]


def part1(data):

    accumulator = 0
    current = 0
    visited = []

    while current not in visited:
        visited.append(current)

        if data[current][0] == 'acc':
            accumulator += int(data[current][1])
            current += 1

        elif data[current][0] == 'nop':
            current += 1

        elif data[current][0] == 'jmp':
            current += int(data[current][1])

        if current >= len(data):
            return(1,accumulator)

    return(0,accumulator)

print("Day 8.1: ", part1(data)[1])

def part2(data):
    acc_list =[]
    for i in range(0,len(data)):
        new_data = copy.deepcopy(data)
        if data[i][0] == 'nop': new_data[i][0] = 'jmp'
        elif data[i][0] == 'jmp': new_data[i][0] = 'nop'

        result = part1(new_data)
        if result[0] == 1: return result[1]


print("Day 8.2: ", part2(data))
