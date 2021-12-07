import math
with open('input.txt') as f:
  for line in f:
  	crabs = [int(x) for x in line.split(',')]

sorted_crabs = sorted(crabs)
best_position = int(math.floor(sum(sorted_crabs) / len(sorted_crabs)))

fuel = 0
for c in sorted_crabs:
	diff = abs(c - best_position)
	triangularNumber = int(diff*(diff+1)/2)
	fuel += triangularNumber

print(fuel)