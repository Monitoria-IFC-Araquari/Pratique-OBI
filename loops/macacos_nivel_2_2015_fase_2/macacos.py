n = int(input())
trees = [tuple(map(int, input().split())) for _ in range(n)]
trees.sort(key=lambda x: x[0])

x = [t[0] for t in trees]
h = [t[1] for t in trees]

def ccw(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

nxt = [n - 1] * n
stack = []
for i in range(n - 1, -1, -1):
    while len(stack) >= 2 and ccw(x[i], h[i], x[stack[-1]], h[stack[-1]], x[stack[-2]], h[stack[-2]]) >= 0:
        stack.pop()
    if stack:
        nxt[i] = stack[-1]
    stack.append(i)

prv = [0] * n
stack = []
for i in range(n):
    while len(stack) >= 2 and ccw(x[stack[-2]], h[stack[-2]], x[stack[-1]], h[stack[-1]], x[i], h[i]) >= 0:
        stack.pop()
    if stack:
        prv[i] = stack[-1]
    stack.append(i)

from collections import deque
q = deque([0])
dist = [-1] * n
dist[0] = 0
while q:
    u = q.popleft()
    if u == n - 1:
        print(dist[u])
        break
    v = nxt[u]
    if v > u and dist[v] == -1:
        dist[v] = dist[u] + 1
        q.append(v)
    v = prv[u]
    if v < u and dist[v] == -1:
        dist[v] = dist[u] + 1
        q.append(v)
    if u + 1 < n and dist[u + 1] == -1:
        dist[u + 1] = dist[u] + 1
        q.append(u + 1)
    if u - 1 >= 0 and dist[u - 1] == -1:
        dist[u - 1] = dist[u] + 1
        q.append(u - 1)
