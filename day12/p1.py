from collections import defaultdict
hsh = defaultdict(list)
with open('input.txt') as f:
	for line in f:
		li = line.strip().split('-')
		hsh[li[0]].append(li[1])
		hsh[li[1]].append(li[0])

paths = []
def go_find_end(hsh, node, seen, path):
	path.append(node)
	if node == 'end':
		global paths
		paths.append(path[:])
		path.pop()
		return

	if node.islower():
		seen.add(node)
	for neighbor in hsh[node]:
		if neighbor not in seen:
			go_find_end(hsh, neighbor, seen, path)

	path.pop()
	if node in seen:
		seen.remove(node)


seen = set()
path = []
go_find_end(hsh, 'start', seen, path)
print(len(paths))