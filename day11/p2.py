grid = []
count = 0
with open('input.txt') as f:
	for line in f:
		grid.append([])
		for num in line.strip():
			grid[-1].append(int(num))


def get_neighbors(row, col):
	res = []
	if row > 0:
		if col > 0:
			res.append((row - 1, col - 1))
		res.append((row - 1, col))
		if col < len(grid[0]) - 1:
			res.append((row - 1, col + 1))

	if col > 0:
		res.append((row, col - 1))
	if col < len(grid[0]) - 1:
		res.append((row, col + 1))

	if row < len(grid) - 1:
		if col > 0:
			res.append((row + 1, col - 1))
		res.append((row + 1, col))
		if col < len(grid[0]) - 1:
			res.append((row + 1, col + 1))
	return res

def flash(row, col, flashed):
	global count
	count += 1
	flashed.add((row, col))
	ns = get_neighbors(row, col)
	for n_row, n_col in ns:
		if (n_row, n_col) not in flashed:
			grid[n_row][n_col] += 1
			if grid[n_row][n_col] > 9:
				flashed.add((n_row, n_col))
				flash(n_row, n_col, flashed)

step = 0
while True:
	step += 1
	flashed = set()
	c = 0
	for row, rowval in enumerate(grid):
		for col, colval in enumerate(rowval):
			grid[row][col] += 1
			if grid[row][col] > 9 and (row, col) not in flashed:
				flash(row, col, flashed)

	for row, rowval in enumerate(grid):
		for col, colval in enumerate(rowval):
			if grid[row][col] > 9:
				grid[row][col] = 0
				c += 1
	if c == len(grid) * len(grid[0]):
		print(step)
		break
