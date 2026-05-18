import sys
sys.setrecursionlimit(1 << 20)

N, K = map(int, input().split())
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

out_lines = []
for _ in range(K):
    parts = input().split()
    if parts[0] == 'F':
        union(int(parts[1]), int(parts[2]))
    else:
        a, b = int(parts[1]), int(parts[2])
        out_lines.append('S' if find(a) == find(b) else 'N')
sys.stdout.write('\n'.join(out_lines))
