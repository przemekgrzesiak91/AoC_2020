import itertools
import numpy as np

data = [int(x) for x in open('data/day1.txt')]
#print(data)

def sum_to_2020(data,n):
    combinations = itertools.combinations(data, n)
    for comb in combinations:
        if sum(comb) == 2020:
            return np.prod(comb)


print("Day 1.1: ", sum_to_2020(data,2))
print("Day 1.2: ", sum_to_2020(data,3))