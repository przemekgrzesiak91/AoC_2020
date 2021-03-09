data = [list(line.strip().split(' ')) for line in open('data/day8.txt')]

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

print("Day 8.1: ", accumulator)


