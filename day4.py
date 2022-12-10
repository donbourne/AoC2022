import numpy as np

def contains(arr):
    if arr[0][0] <= arr[1][0] and arr[0][1] >= arr[1][1]:
        return True
    if arr[1][0] <= arr[0][0] and arr[1][1] >= arr[0][1]:
        return True
    return False

def overlaps(arr):
    return arr[0][0] <= arr[1][1] and arr[0][1] >= arr[1][0]

# read input
start_end = list()
with open("day4.txt", "rt") as f:
    for line in f:
        pairs = line.strip().split(",")
        start_end.append((pairs[0].split("-"), pairs[1].split("-")))

start_end_np = np.array(start_end, dtype=int)

# count pairs where one range fully contains the other
contained_count = 0
overlap_count = 0
for pair in start_end_np:
    if contains(pair):
        contained_count += 1
    if overlaps(pair):
        overlap_count += 1

print(f'contained_count: {contained_count}, overlap_count = {overlap_count}')