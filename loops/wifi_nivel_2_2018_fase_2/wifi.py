import sys

sys.setrecursionlimit(2000000)

n = int(sys.stdin.readline())
rects = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 < y2:
        y1, y2 = y2, y1
    rects.append((x1, y1, x2, y2, _))

area = lambda r: (r[2] - r[0]) * (r[1] - r[3])
rects.sort(key=area, reverse=True)

parent = [-1] * n
children = [[] for _ in range(n)]

for i in range(n):
    x1i, y1i, x2i, y2i, idi = rects[i]
    for j in range(i):
        x1j, y1j, x2j, y2j, idj = rects[j]
        if x1j < x1i and x2j > x2i and y1j > y1i and y2j < y2i:
            if parent[i] == -1 or area(rects[j]) < area(rects[parent[i]]):
                parent[idi] = idj

for i in range(n):
    if parent[i] != -1:
        children[parent[i]].append(i)

def compress(u):
    stack = [u]
    while len(children[stack[-1]]) == 1:
        stack.append(children[stack[-1]][0])
    return stack[-1]

leaves = 0
for i in range(n):
    if not children[i]:
        root = i
        while parent[root] != -1:
            p = parent[root]
            if len(children[p]) == 1:
                root = p
            else:
                break
        if root == i:
            leaves += 1

print(leaves)
