import heapq
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

def neighbor_positions(f, row, col):
	res = []
	if row + 1 < len(f):
		res.append((row + 1, col))
	if col + 1 < len(f[0]):
		res.append((row, col + 1))
	if col - 1 >= 0:
		res.append((row, col - 1))
	if row - 1 >= 0:
		res.append((row - 1, col))

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
			low_points.append((row, col))

counts = []
for row, col in low_points:
	count = 0
	seen = set()
	stack = [(row, col)]
	while len(stack):
		count += 1
		pos = stack.pop()
		r = pos[0]
		c = pos[1]
		seen.add((r, c))
		for n in neighbor_positions(grid, r, c):
			if grid[n[0]][n[1]] != 9 and (n[0], n[1]) not in seen:
				stack.append((n[0], n[1]))
				seen.add((n[0], n[1]))
	counts.append(count)

ret = heapq.nlargest(3, counts)
mult = 1
for r in ret:
	mult *= r
	
print(mult)



