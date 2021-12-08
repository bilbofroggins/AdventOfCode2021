with open('input.txt') as f:
	count = 0
	unique_digits = set([2,3,4,7])
	for line in f:
		line = line.split(' | ')
		digits = line[1].strip().split(' ')
		for d in digits:
			if len(d) in unique_digits:
				count +=1

	print(count)