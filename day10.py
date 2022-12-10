cycle = 1
x_reg = 1

signal_strengths = list()
positions = list()
positions.append(1)

with open("day10.txt", "rt") as f:
    for line in f:
        line = line.strip()
        if line.startswith("noop"):
            cycle += 1
            if (cycle-20) % 40 == 0:
                signal_strengths.append(cycle * x_reg)
            positions.append(x_reg)

        else:
            # first cycle
            cycle += 1
            positions.append(x_reg)
            if (cycle-20) % 40 == 0:
                signal_strengths.append(cycle * x_reg)

            # second cycle
            cycle += 1
            size = int(line.split(" ")[1])
            x_reg += size
            positions.append(x_reg)
            if (cycle-20) % 40 == 0:
                signal_strengths.append(cycle * x_reg)

signal_strength_sum = 0
for cycle in range(1, len(positions)+1):
    if (cycle-1) % 40 == 0:
        print()

    if (cycle - 20) % 40 == 0:
        signal_strength_sum += (cycle * positions[cycle-1])

    crt_row = int((cycle-1)/40)
    crt_col = (cycle-1) % 40
    if crt_col in range(positions[cycle-1]-1, positions[cycle-1]+2):
        print("#", end="")
    else:
        print(" ", end="")

print(signal_strength_sum)