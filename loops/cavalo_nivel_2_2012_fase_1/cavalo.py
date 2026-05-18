n = int(input())
mv = list(map(int, input().split()))

holes = {(1, 3), (2, 3), (2, 5), (5, 4)}
knight = [(2, 1), (1, 2), (-1, 2), (-2, 1),
          (-2, -1), (-1, -2), (1, -2), (2, -1)]

x, y = 4, 3
for i, m in enumerate(mv):
    dx, dy = knight[m - 1]
    x += dx
    y += dy
    if (x, y) in holes:
        print(i + 1)
        break
else:
    print(n)
