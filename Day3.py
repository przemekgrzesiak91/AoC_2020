data = [line.strip() for line in open('data/day3.txt','r').readlines()]

def count_trees(data,x_step,y_step):

    counter = 0
    nrow = len(data)
    ncol = len(data[0])
    x, y = 0, 0

    while y < nrow - 1:
        x += x_step
        y += y_step

        if x > ncol - 1: x = x - ncol
        if data[y][x] == '#': counter += 1

    return counter

print("Day 3.1: ", count_trees(data, 3, 1))
print("Day 3.2: ", count_trees(data, 1, 1) \
                *  count_trees(data, 3, 1) \
                *  count_trees(data, 5, 1) \
                *  count_trees(data, 7, 1) \
                *  count_trees(data, 1, 2))
