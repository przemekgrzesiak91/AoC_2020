data = [line.replace('\n',' ') for line in open('data/day6.txt','r').read().split('\n\n')]
print(data)

# 6.1
n_questions = [len(set(line.replace(' ',''))) for line in data]

# 6.2
n_all_yes = [len(list(set.intersection(*map(set, line.split())))) for line in data]

print("Day 6.1: ", sum(n_questions))
print("Day 6.2: ", sum(n_all_yes))