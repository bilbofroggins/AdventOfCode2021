import math
with open('input.txt') as f:
  for line in f:
  	crabs = [int(x) for x in line.split(',')]

best_position = int(math.floor(sum(crabs) / len(crabs)))

fuel = 0
for c in crabs:
	diff = abs(c - best_position)
	triangular_number = int(diff*(diff+1)/2)
	fuel += triangular_number

print(fuel)