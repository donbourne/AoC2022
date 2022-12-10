import numpy as np


def isVisible(grid, row, col):
    if row == 0 or row == grid.shape[0] - 1 or col == 0 or col == grid.shape[1] - 1:
        return True

    height = grid[row][col]
    if np.sum(grid[row, 0:col] >= height) == 0 or \
            np.sum(grid[0:row, col] >= height) == 0 or \
            np.sum(grid[row, col + 1:] >= height) == 0 or \
            np.sum(grid[row + 1:, col] >= height) == 0:
        return True
    return False


def scenic_score(grid, row, col):
    height = grid[row][col]
    ge_trees = grid >= height

    score_l = 0
    for test_col in range(col-1, -1, -1):
        score_l += 1
        if ge_trees[row, test_col]:
            break

    score_u = 0
    for test_row in range(row-1, -1, -1):
        score_u += 1
        if ge_trees[test_row, col]:
            break

    score_r = 0
    for test_col in range(col+1, grid.shape[1]):
        score_r += 1
        if ge_trees[row, test_col]:
            break

    score_d = 0
    for test_row in range(row+1, grid.shape[0]):
        score_d += 1
        if ge_trees[test_row, col]:
            break

    return score_l * score_u * score_r * score_d

lines = list()
with open("day8.txt", "rt") as f:
    for line in f:
        lines.append(list(line.strip()))

lines_np = np.array(lines, dtype=int)
# print(lines_np)

visible_count = 0
max_score = 0
for row in range(lines_np.shape[0]):
    for col in range(lines_np.shape[1]):
        # problem 1
        if isVisible(lines_np, row, col):
            visible_count += 1
        # problem 2
        score = scenic_score(lines_np, row, col)
        if score > max_score:
            max_score = score
print(visible_count, max_score)