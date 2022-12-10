import numpy as np

with open("day1.txt", "rt") as f:
    total = 0
    max_total = 0
    for line in f:
        line = line.strip()
        if line != "":
            total += int(line)
            if total > max_total:
                max_total = total
        else:
            total = 0

print(f'max: {max_total}')

with open("day1.txt", "rt") as f:
    lines = f.readlines()

elf_total = list()
elf_total.append(0)
elf_index = 0
for line in lines:
    line = line.strip()
    # print(line)
    if line == "":
        elf_index += 1
        elf_total.append(0)
    else:
        current_value = elf_total.pop()
        current_value += int(line)
        elf_total.append(current_value)

# print the total from the 3 elves with the most food
elf_total_np = np.array(elf_total)
elf_total_np = np.sort(elf_total_np)[::-1]
print(f'total from top 3 elves: {np.sum(elf_total_np[0:3])}')

