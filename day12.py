import sys
import numpy as np

np.set_printoptions(linewidth=1024)
np.set_printoptions(threshold=sys.maxsize)

# compute ordinals
def ordinal(height):
    if height == 'S':
        height = 'a'
    elif height == 'E':
        height = 'z'
    return ord(height)


heights = list()
with open("day12.txt", "rt") as f:
    for line in f:
        heights_line = list(line.strip())
        heights.append(heights_line)
# print(heights)

start_cell = end_cell = (0,0)
all_cells_ordinal = np.zeros((len(heights), len(heights[0])), dtype=int)
for row in range(len(heights)):
    for col in range(len(heights[0])):
        height = heights[row][col]
        all_cells_ordinal[row,col] = ordinal(height)
        if height == 'S':
            start_cell = (row, col)
        elif height == 'E':
            end_cell = (row, col)
rows, cols = all_cells_ordinal.shape
# print(all_cells_ordinal, start_cell, end_cell, rows, cols)

all_cells_best_number = np.ones(all_cells_ordinal.shape, dtype=int)
all_cells_best_number *= -1
all_cells_best_number[end_cell] = 0
# print(all_cells_best_number)

cells_previous_number_rows = list()
cells_previous_number_cols = list()
cells_previous_number_rows.append(end_cell[0])
cells_previous_number_cols.append(end_cell[1])


def get_next_cells(row, col, cells_next_number_rows, cells_next_number_cols):
    min_ordinal = all_cells_ordinal[row,col] - 1
    filled_some_cells = False

    if row > 0:
        if all_cells_best_number[row-1, col] == -1:
            if all_cells_ordinal[row-1, col] >= min_ordinal:
                cells_next_number_rows.append(row-1)
                cells_next_number_cols.append(col)
                filled_some_cells = True
    if col > 0:
        if all_cells_best_number[row, col-1] == -1:
            if all_cells_ordinal[row, col-1] >= min_ordinal:
                cells_next_number_rows.append(row)
                cells_next_number_cols.append(col-1)
                filled_some_cells = True
    if row+1 < rows:
        if all_cells_best_number[row+1, col] == -1:
            if all_cells_ordinal[row+1, col] >= min_ordinal:
                cells_next_number_rows.append(row+1)
                cells_next_number_cols.append(col)
                filled_some_cells = True
    if col+1 < cols:
        if all_cells_best_number[row, col+1] == -1:
            if all_cells_ordinal[row, col+1] >= min_ordinal:
                cells_next_number_rows.append(row)
                cells_next_number_cols.append(col+1)
                filled_some_cells = True
    return filled_some_cells


current_number = 0
filled_some_cells = True
ordinal_a = ordinal('a')
while filled_some_cells == True:
    filled_some_cells = False
    current_number += 1
    cells_next_number_rows = list()
    cells_next_number_cols = list()
    for i in range(len(cells_previous_number_rows)):
        if get_next_cells(cells_previous_number_rows[i], cells_previous_number_cols[i], cells_next_number_rows, cells_next_number_cols):
            filled_some_cells = True
    # print(cells_next_number_rows, cells_next_number_cols)

    all_cells_best_number[cells_next_number_rows, cells_next_number_cols] = current_number
    # this has benefit of not having any dups (so using this instead of setting previous to next)
    cells_previous_number_rows, cells_previous_number_cols = np.nonzero(all_cells_best_number == current_number)
    # print(all_cells_best_number)

print(all_cells_best_number)
print(f'fewest steps = {all_cells_best_number[start_cell]}')
all_cells_best_number[np.nonzero(all_cells_best_number == -1)] = 999
print(f'fewest steps from elevation "a": {np.min(all_cells_best_number[np.nonzero(all_cells_ordinal == ordinal_a)])}')
