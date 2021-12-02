f = open('input.txt')
lines = f.readlines()

depth = 0
length = 0
for line in lines:
	instructions = line.rstrip().split(' ')

	direction = instructions[0]
	mag = int(instructions[1])
	
	if direction == 'forward':
		length += mag
	elif direction == 'down':
		depth += mag
	else:
		depth -= mag
		if depth < 0:
			depth = 0

print(depth*length)