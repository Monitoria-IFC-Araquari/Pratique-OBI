import sys
from collections import deque

sys.setrecursionlimit(2000000)
n = int(sys.stdin.readline())
adj = [[] for _ in range(n)]
for i in range(n):
    parts = list(map(int, sys.stdin.readline().split()))
    m = parts[0]
    for x in parts[1:]:
        j = x - 1
        adj[i].append(j)
        adj[j].append(i)

color = [-1] * n
color[0] = 0
q = deque([0])
while q:
    u = q.popleft()
    for v in adj[u]:
        if color[v] == -1:
            color[v] = 1 - color[u]
            q.append(v)

team1 = [str(i + 1) for i in range(n) if color[i] == 0]
team2 = [str(i + 1) for i in range(n) if color[i] == 1]
print(" ".join(team1))
print(" ".join(team2))
