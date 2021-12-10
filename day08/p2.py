trials = []
outputs = []
with open('input.txt') as f:
	count = 0
	unique_digits = set([2,3,4,7])
	for line in f:
		line = line.split(' | ')
		trials.append(line[0].strip().split(' '))
		outputs.append(line[1].strip().split(' '))


def get_digit_str(segments):
	segments = set(segments)
	if len(segments) == 2:
		return '1'
	elif len(segments) == 3:
		return '7'
	elif len(segments) == 4:
		return '4'
	elif len(segments) == 7:
		return '8'
	elif len(segments) == 5:
		if 'c' not in segments:
			return '5'
		elif 'e' in segments:
			return '2'
		else:
			return '3'
	elif len(segments) == 6:
		if 'd' not in segments:
			return '0'
		elif 'c' in segments:
			return '9'
		else:
			return '6'

'''
segments - number
2 - 1
3 - 7
4 - 4
5 - 2,3,5
6 - 0,6,9
7 - 8

1, 7(deduce A), 6(deduce C,F), 4, 0(deduce B,D), 9(deduce E,G)
'''

total = 0
for i, trial in enumerate(trials):
	hsh = {2:[],3:[],4:[],5:[],6:[],7:[]}

	running_list = set(['a','b','c','d','e','f','g'])
	mapping = {'a':None,'b':None,'c':None,'d':None,'e':None,'f':None,'g':None}
	for digit in trial:
		hsh[len(digit)].append(digit)

	one_chars = set(hsh[2][0])
	seven_chars = set(hsh[3][0])
	mapping[list(seven_chars - one_chars)[0]] = 'a'
	running_list.remove(list(seven_chars - one_chars)[0])

	for digit in hsh[6]:
		if not(hsh[2][0][0] in digit and hsh[2][0][1] in digit):
			if hsh[2][0][0] in digit:
				mapping[hsh[2][0][0]] = 'f'
				mapping[hsh[2][0][1]] = 'c'
			else:
				mapping[hsh[2][0][1]] = 'f'
				mapping[hsh[2][0][0]] = 'c'
			running_list.remove(hsh[2][0][0])
			running_list.remove(hsh[2][0][1])

	bdchars = list(set(hsh[4][0]) - one_chars)
	for digit in hsh[6]:
		if not(bdchars[0] in digit and bdchars[1] in digit):
			if bdchars[0] in digit:
				mapping[bdchars[0]] = 'b'
				mapping[bdchars[1]] = 'd'
			else:
				mapping[bdchars[1]] = 'b'
				mapping[bdchars[0]] = 'd'
			running_list.remove(bdchars[1])
			running_list.remove(bdchars[0])

	egchars = list(running_list)
	for digit in hsh[6]:
		if not(egchars[0] in digit and egchars[1] in digit):
			if egchars[0] in digit:
				mapping[egchars[0]] = 'g'
				mapping[egchars[1]] = 'e'
			else:
				mapping[egchars[1]] = 'g'
				mapping[egchars[0]] = 'e'

	total_row = ''
	for digit in outputs[i]:
		real_segments = []
		for char in digit:
			real_segments.append(mapping[char])
		total_row += get_digit_str(real_segments)
	total += int(total_row)

print(total)