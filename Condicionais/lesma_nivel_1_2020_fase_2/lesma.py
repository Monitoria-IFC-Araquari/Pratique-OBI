a = int(input())
s = int(input())
d = int(input())
if s >= a:
    print(1)
else:
    print((a - s - 1) // (s - d) + 2)
