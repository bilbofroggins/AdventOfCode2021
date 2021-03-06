from heapq import heappush, heappop
lines = []
with open('input.txt') as f:
    for line in f:
        lines.append(line)

def expandMap(xs):
    t = [ [ (xs[r][c] + i + j - 1) % 9 + 1 for j in range(5) for c in range(len(xs)) ] for i in range(5) for r in range(len(xs)) ]
    return t

def validCoord(xs, coord):
    return coord[0] >= 0 and coord[0] < len(xs) and coord[1] >= 0 and coord[1] < len(xs[0])

def gridGet(xs, coord):
    return xs[coord[0]][coord[1]]

def a_star(xs):
    open = [ (-1, (0, 0)) ]
    g = [ [ -1 for _ in range(len(xs[0])) ] for _ in range(len(xs)) ]
    g[0][0] = 0
    target = (len(xs)-1, len(xs[0])-1)
    while len(open) > 0:
        current = heappop(open)[1]
        if current == target:
            return gridGet(g, current)
        for r, c in [ (1, 0), (0, 1), (-1, 0), (0, -1) ]:
            adj = (current[0]+r, current[1]+c)
            if validCoord(xs, adj):
                oldG, newG = gridGet(g, adj), gridGet(g, current) + gridGet(xs, adj)
                if newG < oldG or oldG == -1:
                    g[adj[0]][adj[1]] = newG
                    h = r + c
                    if adj not in open:
                        heappush(open, (newG + h, adj))

xs = [ [ int(c) for c in line.strip() ] for line in lines ]

print(a_star(expandMap(xs)))