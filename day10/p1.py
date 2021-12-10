hsh = {']':'[', ')':'(', '>':'<', '}':'{'}
illegals = []

points = {')': 3, ']': 57, '}': 1197, '>': 25137}

with open('input.txt') as f:
	for line in f:
		stack = []
		line = line.strip()
		for char in line:
			if len(stack) and char in hsh and stack[-1] == hsh[char]:
				stack.pop()
			elif char not in hsh:
				stack.append(char)
			else:
				illegals.append(char)
				break

total = 0
for illegal in illegals:
	total += points[illegal]

print(total)