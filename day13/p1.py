dots = []
folds = []
row_max = 0
col_max = 0

with open('input.txt') as f:
	for line in f:
		if line[0] == 'f':
			inst = line.strip().split('fold along ')[1]
			direction, pos = inst.split('=')
			folds.append((direction, int(pos)))
		if line[0].isnumeric():
			col, row = line.strip().split(',')
			row_max = max(int(row), row_max)
			col_max = max(int(col), col_max)
			dots.append((int(row), int(col)))

grid = [[0]*(col_max + 1) for _ in range(row_max + 1)]
for row, col in dots:
	grid[row][col] = 1

for direction, pos in folds:
	if direction == 'y':
		if pos < len(grid) / 2:
			for row in range(pos):
				or_row = pos + (pos - row)
				for c in range(len(grid[0])):
					grid[or_row][c] = grid[or_row][c] or grid[row][c]
			grid = grid[pos + 1:]
			grid = grid[::-1]
		else:
			for row in range(pos + 1, len(grid)):
				or_row = pos - (row - pos)
				for c in range(len(grid[0])):
					grid[or_row][c] = grid[or_row][c] or grid[row][c]
			grid = grid[:pos]
	else:
		if pos < len(grid[0]) / 2:
			for col in range(pos):
				or_col = pos + (pos - col)
				for r in range(len(grid)):
					grid[r][or_col] = grid[r][or_col] or grid[r][col]

			for r in range(len(grid)):
				grid[r] = grid[r][pos + 1:][::-1]

		else:
			for col in range(pos + 1, len(grid[0])):
				or_col = pos - (col - pos)
				for r in range(len(grid)):
					grid[r][or_col] = grid[r][or_col] or grid[r][col]
			for r in range(len(grid)):
				grid[r] = grid[:pos]
	break

count = 0
for r in grid:
	for v in r:
		if v == 1:
			count += 1
print(count)