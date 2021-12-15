grid = []
with open('input.txt') as f:
	for line in f:
		grid.append([])
		for num in line.strip():
			grid[-1].append(int(num))

for row in range(len(grid) - 1, -1, -1):
	for col in range(len(grid[0]) - 1, -1, -1):
		if row == len(grid) - 1 and col == len(grid[0]) - 1:
			min_val = grid[-1][-1]
			continue
		elif row == len(grid) - 1:
			min_val = grid[row][col + 1]
		elif col == len(grid[0]) - 1:
			min_val = grid[row + 1][col]
		else:
			min_val = min(grid[row + 1][col], grid[row][col + 1])
		grid[row][col] = grid[row][col] + min_val
		
print(grid[0][0] - 1)