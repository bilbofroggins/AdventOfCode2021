data = []
max_col = 0
max_row = 0

with open('input.txt') as f:
  for line in f:
  	start, stop = line.rstrip('\n').split(' -> ')
  	col1, row1 = start.split(',')
  	col2, row2 = stop.split(',')
  	col1, col2, row1, row2 = int(col1), int(col2), int(row1), int(row2)

  	colmax = max(col1, col2)
  	if colmax > max_col:
  		max_col = colmax
  	rowmax = max(row1, row2)
  	if rowmax > max_row:
  		max_row = rowmax

  	data.append([(row1,col1),(row2,col2)])


grid = [[0]*(max_col + 1) for _ in range(max_row + 1)]

def get_marked_positions(row1, col1, row2, col2):
	res = []
	if col1 == col2:
		col_same = True
		diff = abs(row2 - row1)
	elif row1 == row2:
		col_same = False
		diff = abs(col2 - col1)
	else:
		return []

	for i in range(diff + 1):
		if col_same:
			col = col1
			row = i + min(row1, row2)
		else:
			col = i + min(col1, col2)
			row = row1
		res.append((row, col))
	return res

for line in data:
	row1, col1, row2, col2 = line[0][0], line[0][1], line[1][0], line[1][1]
	positions = get_marked_positions(row1, col1, row2, col2)
	for position in positions:
		grid[position[0]][position[1]] += 1

# for r in grid:
# 	print(r)
count = 0
for row in grid:
	for val in row:
		if val > 1:
			count += 1

print(count)




