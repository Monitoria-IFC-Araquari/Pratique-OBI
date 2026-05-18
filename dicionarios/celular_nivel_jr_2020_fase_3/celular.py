n = int(input())
pts = [tuple(map(int, input().split())) for _ in range(n)]
alc = int(input())
parent = list(range(n))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[a] = b

B = alc
buckets = {}
for idx, (x, y) in enumerate(pts):
    bx, by = x // B, y // B
    key = (bx, by)
    if key in buckets:
        buckets[key].append(idx)
    else:
        buckets[key] = [idx]
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            nk = (bx + dx, by + dy)
            if nk in buckets:
                for j in buckets[nk]:
                    if j != idx:
                        dx_ = pts[idx][0] - pts[j][0]
                        dy_ = pts[idx][1] - pts[j][1]
                        if dx_ * dx_ + dy_ * dy_ <= alc * alc:
                            union(idx, j)

root = find(0)
for i in range(1, n):
    if find(i) != root:
        print('N')
        break
else:
    print('S')
