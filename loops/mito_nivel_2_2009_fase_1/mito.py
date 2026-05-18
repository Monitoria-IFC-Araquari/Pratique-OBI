n = int(input())
visto = set()
repetiu = 0
for _ in range(n):
    x, y = map(int, input().split())
    if (x, y) in visto:
        repetiu = 1
    visto.add((x, y))
print(repetiu)
