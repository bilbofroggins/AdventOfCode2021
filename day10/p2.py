hsh = {']':'[', ')':'(', '>':'<', '}':'{'}
hsh_rev = {'[':']', '(':')', '<':'>', '{':'}'}

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores = []
p2_points = {')': 1, ']': 2, '}': 3, '>': 4}
totals = []

with open('input.txt') as f:
	for line in f:
		illegal = False
		stack = []
		line = line.strip()
		for char in line:
			if len(stack) and char in hsh and stack[-1] == hsh[char]:
				stack.pop()
			elif char not in hsh:
				stack.append(char)
			else:
				illegal = True
		if not illegal:
			totals.append(0)
			while len(stack):
				closing_char = hsh_rev[stack[-1]]
				stack.pop()
				totals[-1] *= 5
				totals[-1] += p2_points[closing_char]

totals.sort()
mid_i = int((len(totals) - 1) / 2)
print(totals[mid_i])