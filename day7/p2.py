import math
with open('input.txt') as f:
  for line in f:
  	crabs = [int(x) for x in line.split(',')]

best_position_low = int(math.floor(sum(crabs) / len(crabs)))
best_position_high = int(round(sum(crabs) / len(crabs)))

fuel_low = 0
for c in crabs:
	diff = abs(c - best_position_low)
	triangular_number = int(diff*(diff+1)/2)
	fuel_low += triangular_number
fuel_high = 0
for c in crabs:
	diff = abs(c - best_position_high)
	triangular_number = int(diff*(diff+1)/2)
	fuel_high += triangular_number

print(min(fuel_low, fuel_high))