import sys


def get_start():
    for rowNumber, row in enumerate(grid):
        for columnNumber, val in enumerate(row):
            if val == '^':
                return (rowNumber, columnNumber)


with open(sys.argv[1], 'r') as file:
    grid = list(map(list, map(str.strip, file.readlines())))

num_rows = len(grid)
num_cols = len(grid)

start_r, start_c = get_start()

def is_Loop():
    r,c = start_r, start_c
    dr, dc = -1, 0
    visited = set()
    while True:
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        if not (0 <= r + dr < num_rows and 0 <= c + dc < num_cols):
            break
        if grid[r + dr][c + dc] == '#':
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
    return False

counter_part2 = 0
for ro in range(num_rows):
    for co in range(num_cols):
        if (grid[ro][co] != '.'):
            continue
        grid[ro][co] = '#'
        if (is_Loop()):
            counter_part2 += 1
        grid[ro][co] = '.'
print(counter_part2)

