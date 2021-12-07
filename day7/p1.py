with open('input.txt') as f:
  for line in f:
  	crabs = [int(x) for x in line.split(',')]

sorted_crabs = sorted(crabs)
best_position = sorted_crabs[len(sorted_crabs) // 2]

fuel = 0
for c in sorted_crabs:
	fuel += abs(c - best_position)

print(fuel)