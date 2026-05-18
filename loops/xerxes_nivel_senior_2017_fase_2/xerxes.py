import sys

n = int(sys.stdin.readline())
dario = 0
for _ in range(n):
    d, x = map(int, sys.stdin.readline().split())
    if (x - d) % 5 == 1 or (x - d) % 5 == 2:
        dario += 1
    else:
        dario -= 1

print("dario" if dario > 0 else "xerxes")
