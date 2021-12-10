f = open('input.txt')
lines = f.readlines()

depth = 0
length = 0
aim = 0
for line in lines:
	instructions = line.rstrip().split(' ')

	direction = instructions[0]
	mag = int(instructions[1])

	if direction == 'forward':
		length += mag
		depth += aim * mag
	elif direction == 'down':
		aim += mag
	else:
		aim -= mag
		if aim < 0:
			aim = 0

print(depth*length)