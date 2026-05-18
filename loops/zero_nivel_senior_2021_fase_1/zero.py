import sys

n = int(sys.stdin.readline())
p = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if p:
            p.pop()
    else:
        p.append(x)
print(sum(p))
