n = int(input())
t = list(map(int, input().split()))
p = int(input())
m = int(input())

c1 = t.count(1)
c2 = t.count(2)

if p >= c1 and m >= c2:
    print('S')
else:
    print('N')
