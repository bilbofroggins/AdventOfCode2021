f = open('input.txt')
lines = f.readlines()

count = []

for i, col in enumerate(zip(*lines)):
	num_rows = len(col)
	count.append(0)
	for num in col:
		if num == '1':
			count[-1] += 1

	if count[-1] > num_rows / 2:
		count[-1] = 1
	else:
		count[-1] = 0

epsilon = [int(not c) for c in count]

c_out = 0
for bit in count:
    c_out = (c_out << 1) | bit

e_out = 0
for bit in epsilon:
    e_out = (e_out << 1) | bit

print(c_out * e_out)