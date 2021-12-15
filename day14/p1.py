from collections import defaultdict
inst = {}
seq = ''
with open('input.txt') as f:
	for i, line in enumerate(f):
		if i == 0:
			seq = line.strip()
		elif i > 1:
			chars, between = line.strip().split(' -> ')
			inst[chars] = between


elem_count = defaultdict(int)
for c in seq:
	elem_count[c] += 1
steps = 10
for x in range(steps):
	temp_str = []
	for i in range(len(seq) - 1):
		two = seq[i:i + 2]
		between = inst[two]
		temp_str.append(two[0])
		temp_str.append(between)
		elem_count[between] += 1
	temp_str.append(seq[-1])

	seq = ''.join(temp_str)

max_count = None
min_count = None
for char, count in elem_count.items():
	if max_count == None:
		max_count = count
	if min_count == None:
		min_count = count
	max_count = max(max_count, count)
	min_count = min(min_count, count)

print(max_count - min_count)

