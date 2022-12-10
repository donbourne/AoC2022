def get_common_letter(sack1, sack2, sack3=list()):
    for c in sack1:
        if c in sack2:
            if len(sack3) == 0 or c in sack3:
                return c


def get_priority(letter):
    if letter.islower():
        return ord(letter) - 96

    return ord(letter) - 38


with open("day3.txt", "rt") as f:
    lines = f.readlines()

print("problem 1")
priority_sum = 0
for line in lines:
    # print(line)
    line_list = list(line.strip())

    sack1 = line_list[0:int(len(line_list)/2)]
    sack2 = line_list[int(len(line_list)/2):]

    common = get_common_letter(sack1, sack2)
    priority = get_priority(common)
    priority_sum += priority
    # print(f'common: {common} priority: {priority} priority_sum: {priority_sum}')

print(f'priority_sum: {priority_sum}')


print("problem 2")
priority_sum = 0
group_lines = list()
lines2 = list()
for line in lines:
    lines2.append(line.strip())

for i in range(int(len(lines2)/3)):
    group_lines.append(lines2[i*3:i*3+3])

for g in group_lines:
    common = get_common_letter(g[0], g[1], g[2])
    priority = get_priority(common)
    priority_sum += priority
    # print(f'common: {common} priority: {priority} priority_sum: {priority_sum}')

print(f'priority_sum: {priority_sum}')
