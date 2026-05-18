pts = []
for _ in range(7):
    x, y = map(int, input().split())
    pts.append((x, y))

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def sqlen(a):
    return a[0] * a[0] + a[1] * a[1]

def collinear(p, q, r):
    return cross(sub(q, p), sub(r, p)) == 0

p1, p2, p3, p4, p5, p6, p7 = pts

v12 = sub(p2, p1)
v13 = sub(p3, p1)

cond1 = dot(v12, v13) > 0
cond2 = sqlen(v12) == sqlen(v13)
cond3 = collinear(p2, p3, p4) and collinear(p2, p3, p5)

mid23 = (p2[0] + p3[0], p2[1] + p3[1])
mid45 = (p4[0] + p5[0], p4[1] + p5[1])
cond4 = mid23 == mid45

len23 = sqlen(sub(p2, p3))
len45 = sqlen(sub(p4, p5))
cond5 = len23 > len45

v23 = sub(p3, p2)
v46 = sub(p6, p4)
v57 = sub(p7, p5)
cond6 = dot(v46, v23) == 0 and dot(v57, v23) == 0
cond7 = sqlen(v46) == sqlen(v57)

cp1 = cross(v23, sub(p1, p2))
cp6 = cross(v23, sub(p6, p2))
cond8 = (cp1 > 0 and cp6 < 0) or (cp1 < 0 and cp6 > 0)

print('S' if (cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7 and cond8) else 'N')
