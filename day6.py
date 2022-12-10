# get number of chars in line until n unique
def num_chars(line, n):
    for i in range((n-1), len(line)):
        if len(set(line[i-(n-1):i+1])) == n:
            return i+1


with open("day6.txt", "rt") as f:
    for line in f:
        print(f' 4: {num_chars(line, 4)}')
        print(f'14: {num_chars(line, 14)}')
