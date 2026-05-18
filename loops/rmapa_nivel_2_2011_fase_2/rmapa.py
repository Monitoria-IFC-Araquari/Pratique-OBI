N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, c = map(int, input().split())
    edges.append((c, u - 1, v - 1))
edges.sort()
parent = list(range(N))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    parent[a] = b
    return True
cost = 0
for c, u, v in edges:
    if union(u, v):
        cost += c
print(cost)
