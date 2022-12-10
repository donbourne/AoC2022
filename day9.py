def compute_next_head_position(current_head_position, move_direction, move_steps):
    next_head_row, next_head_col = current_head_position
    match move_direction:
        case "R":
            next_head_col += move_steps
        case "U":
            next_head_row -= move_steps
        case "L":
            next_head_col -= move_steps
        case "D":
            next_head_row += move_steps

    return next_head_row, next_head_col


def compute_next_tail_position(current_tail_position, next_head_position):
    current_tail_row, current_tail_col = current_tail_position
    next_head_row, next_head_col = next_head_position

    next_tail_row = current_tail_row
    next_tail_col = current_tail_col

    if next_head_row in range(current_tail_row - 1, current_tail_row + 2) \
            and next_head_col in range(current_tail_col - 1, current_tail_col + 2):
        return next_tail_row, next_tail_col

    if next_head_row < current_tail_row:
        next_tail_row -= 1
    elif next_head_row > current_tail_row:
        next_tail_row += 1

    if next_head_col > current_tail_col:
        next_tail_col += 1
    elif next_head_col < current_tail_col:
        next_tail_col -= 1

    return next_tail_row, next_tail_col


current_head_position = (0,0)
head_positions = [(0,0)]
with open("day9.txt", "rt") as f:
    for line in f:
        direction, steps = line.strip().split(" ")
        steps = int(steps)
        for i in range(steps):
            current_head_position = compute_next_head_position(current_head_position, direction, 1)
            head_positions.append(current_head_position)
# print(head_positions)

# problem 1
current_tail_position = (0,0)
tail_positions = [(0,0)]
tail_positions_set = set([(0,0)])
for i, head_position in enumerate(head_positions):
    if i == 0:
        continue
    current_tail_position = compute_next_tail_position(current_tail_position, head_position)
    tail_positions.append(current_tail_position)
    tail_positions_set.add(current_tail_position)
# print(tail_positions)
# print(tail_positions_set)
print(len(tail_positions_set))

# problem 2
current_tail_position = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
tail_positions = [[(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)], [(0,0)]]
tail_positions_set = [set([(0,0)]), set([(0,0)]), set([(0,0)]), set([(0,0)]), set([(0,0)]), set([(0,0)]), set([(0,0)]),
                      set([(0,0)]), set([(0,0)])]
for i, head_position in enumerate(head_positions):
    if i == 0:
        continue
    for k in range(9):
        if k == 0:
            current_tail_position[k] = compute_next_tail_position(current_tail_position[k], head_position)
        else:
            current_tail_position[k] = compute_next_tail_position(current_tail_position[k], current_tail_position[k-1])
        tail_positions[k].append(current_tail_position[k])
        tail_positions_set[k].add(current_tail_position[k])
# print(tail_positions[8])
# print(tail_positions_set[8])
print(len(tail_positions_set[8]))
