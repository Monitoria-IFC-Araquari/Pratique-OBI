n, m, ins = map(int, input().split())
age = [0] + list(map(int, input().split()))
parent = [0] * (n + 1)
children = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    parent[y] = x
    children[x].append(y)

for _ in range(ins):
    parts = input().split()
    if parts[0] == 'P':
        e = int(parts[1])
        ans = 10**9
        v = e
        while parent[v] != 0:
            v = parent[v]
            if age[v] < ans:
                ans = age[v]
        if ans == 10**9:
            print('*')
        else:
            print(ans)
    else:
        a, b = int(parts[1]), int(parts[2])
        pa, pb = parent[a], parent[b]
        ca, cb = children[a][:], children[b][:]
        if pa != 0:
            children[pa].remove(a)
            children[pa].append(b)
        if pb != 0:
            children[pb].remove(b)
            children[pb].append(a)
        parent[a], parent[b] = pb, pa
        children[a], children[b] = cb, ca
        for c in children[a]:
            parent[c] = a
        for c in children[b]:
            parent[c] = b
