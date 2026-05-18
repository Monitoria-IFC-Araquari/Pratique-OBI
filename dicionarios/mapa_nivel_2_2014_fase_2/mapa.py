N = int(input())
parent = list(range(N + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[a] = b

for _ in range(N - 1):
    A, B, C = map(int, input().split())
    if C == 0:
        union(A, B)

comp_size = {}
for i in range(1, N + 1):
    r = find(i)
    comp_size[r] = comp_size.get(r, 0) + 1

total = N * (N - 1) // 2
for sz in comp_size.values():
    total -= sz * (sz - 1) // 2
print(total)
