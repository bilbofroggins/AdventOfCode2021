arr = [1,2,3,3,4]

count = 0
last = arr[0]
for num in arr:
	if num > last:
		count += 1
	last = num

print(count)