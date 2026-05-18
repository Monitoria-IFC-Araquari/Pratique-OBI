n, m = map(int, input().split())
casas = list(map(int, input().split()))
entregas = list(map(int, input().split()))

pos = {c: i for i, c in enumerate(casas)}

cur = 0
total = 0
for e in entregas:
    p = pos[e]
    total += abs(p - cur)
    cur = p

print(total)
