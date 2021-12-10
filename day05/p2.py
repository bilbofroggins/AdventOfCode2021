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
	col_same, row_same, same = False, False, False
	if col1 == col2:
		col_same = True
		diff = abs(row2 - row1)
	elif row1 == row2:
		row_same = True
		diff = abs(col2 - col1)
	elif (row2 - row1) * (col2 - col1) > 0:
		same = True
		#9,3/7,1 -> 9,3 8,2 7,1
		diff = abs(row2 - row1)
	else:
		#9,1/7,3 -> 9,1 8,2 7,3
		diff = abs(row2 - row1)


	for i in range(diff + 1):
		if col_same:
			col = col1
			row = i + min(row1, row2)
		elif row_same:
			col = i + min(col1, col2)
			row = row1
		elif same:
			row = i + min(row1, row2)
			col = i + min(col1, col2)
		else:
			row = i + min(row1, row2)
			col = max(col1, col2) - i
		res.append((row, col))
	return res

for line in data:
	row1, col1, row2, col2 = line[0][0], line[0][1], line[1][0], line[1][1]
	positions = get_marked_positions(row1, col1, row2, col2)
	for position in positions:
		grid[position[0]][position[1]] += 1

count = 0
for row in grid:
	for val in row:
		if val > 1:
			count += 1

print(count)




