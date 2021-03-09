import math

def seat_ID(data):
    start = 0
    stop = 127
    for char in data[0:7]:
        if char == "F": stop =  stop - math.floor((stop-start)/2) -1
        elif char == "B": start = stop - math.ceil((stop-start)/2) +1
    row = start

    start = 0
    stop = 7
    for char in data[7:]:
        if char == "L": stop =  stop - math.floor((stop-start)/2) -1
        elif char == "R": start = stop - math.ceil((stop-start)/2) +1
    column = start

    ID = row * 8 + column

    return ID

data = [line.strip() for line in open('data/day5.txt','r')]
seat_IDs = []

for line in data:
    seat_IDs.append(seat_ID(line))

last_seat = max(seat_IDs)

# 5.2
first_seat = min(seat_IDs)
all_seats = list(range(first_seat,last_seat))

for ID in all_seats:
    if ID not in seat_IDs:
        my_ID = ID


print("Day 5.1: ", last_seat)
print("Day 5.2: ", my_ID)
