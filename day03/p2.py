f = open('input.txt')
lines = f.readlines()

def whittle(lines, oxygen):
	i = 0
	while len(lines) > 1:
		zeros = []
		ones = []
		col = list(zip(*lines))[i]
		count = 0
		for row, num in enumerate(col):
			if num == '1':
				ones.append(row)
			else:
				zeros.append(row)

		if oxygen:
			if len(ones) >= len(zeros):
				lines = [lines[one] for one in ones]
			else:
				lines = [lines[zero] for zero in zeros]
		else:
			if len(ones) >= len(zeros):
				lines = [lines[zero] for zero in zeros]
			else:
				lines = [lines[one] for one in ones]
		i += 1

	return lines[0].rstrip()

oxy = whittle(lines, True)
co2 = whittle(lines, False)

oxy_out = 0
for bit in oxy:
    oxy_out = (oxy_out << 1) | int(bit)
co2_out = 0
for bit in co2:
    co2_out = (co2_out << 1) | int(bit)

print(oxy_out * co2_out)