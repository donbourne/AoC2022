import copy


# print top of each stack
def print_top_of_stacks(stacks):
    # print top of each stack
    for stack in stacks:
        print(stack[-1], end='')
    print()


with open("day5.txt", "rt") as f:
    lines = f.readlines()

moves = list()
crates = list()
for line in lines:
    line = line.replace("\n", "")
    if line.find("[") >= 0:
        crates.append(line[1::4])
    elif line.find("move") >= 0:
        num, source, target = line.replace("move ", "").replace(" from ", "-").replace(" to ", "-").split("-")
        moves.append((int(num), int(source), int(target)))
    elif line != "":
        num_stacks = int(len(line) / 4) + 1

stacks = list()
for i in range(num_stacks):
    stacks.append(list())

# fill the stacks
crates.reverse()
for crate_row in crates:
    for col, crate_col in enumerate(crate_row):
        if crate_col != " ":
            stacks[col].append(crate_col)

# problem 1
stacks1 = copy.deepcopy(stacks)
for num, source, target in moves:
    for i in range(num):
        stacks1[target - 1].append(stacks1[source - 1].pop())
print_top_of_stacks(stacks1)

# problem 2
stacks2 = copy.deepcopy(stacks)
for num, source, target in moves:
    stacks2[target - 1].extend(stacks2[source - 1][-num:])
    for i in range(num):
        stacks2[source - 1].pop()
print_top_of_stacks(stacks2)