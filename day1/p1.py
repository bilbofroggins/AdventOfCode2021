with open('input.txt') as f:
  arr = [int(line.rstrip('\n')) for line in f]

count = 0
last = arr[0]
for num in arr:
	if num > last:
		count += 1
	last = num

print(count)