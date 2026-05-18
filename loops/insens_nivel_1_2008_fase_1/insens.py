n = int(input())
total = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    total += (x1 - x2) ** 2 + (y1 - y2) ** 2
print(total)
