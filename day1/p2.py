arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]

count = 0
last = arr[0] + arr[1] + arr[2]
for i in range(1, len(arr) - 2):
	s = arr[i] + arr[i + 1] + arr[i + 2]
	if s > last:
		count += 1
	last = s

print(count)