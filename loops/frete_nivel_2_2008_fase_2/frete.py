N, M = map(int, input().split())
edges = []
for _ in range(M):
    P, Q, U = map(int, input().split())
    edges.append((U, P, Q))
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
total = 0
for U, P, Q in edges:
    if union(P, Q):
        total += U
print(total)
