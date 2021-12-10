grid = []
low_points = []

def neighbors(f, row, col):
	res = []
	if row + 1 < len(f):
		res.append(f[row + 1][col])
	if col + 1 < len(f[0]):
		res.append(f[row][col + 1])
	if col - 1 >= 0:
		res.append(f[row][col - 1])
	if row - 1 >= 0:
		res.append(f[row - 1][col])

	return res

with open('input.txt') as f:
	for line in f:
		line = line.strip()
		grid.append([])
		for num in line:
			grid[-1].append(int(num))

for row, r in enumerate(grid):
	for col, num in enumerate(r):
		if num < min(neighbors(grid, row, col)):
			low_points.append(num)

total = 0
for point in low_points:
	total += point + 1
print(total)