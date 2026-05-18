v = int(input())
p = int(input())
base = v // p
r = v % p
for i in range(p):
    print(base + (1 if i < r else 0))
