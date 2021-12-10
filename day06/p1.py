with open('input.txt') as f:
  for line in f:
  	nums = line.split(',')

hsh = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
for num in nums:
	hsh[int(num)] += 1

days = 80

for _ in range(days):
	temp = 0
	for i in range(8, -2, -1):
		if i < 0:
			hsh[6] += temp
			hsh[8] += temp
			break
		hsh[i], temp = temp, hsh[i]

count = 0
for n in hsh:
	count += hsh[n]

print(count)