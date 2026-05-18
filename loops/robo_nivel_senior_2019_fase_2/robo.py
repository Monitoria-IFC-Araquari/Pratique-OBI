from collections import deque
xi, yi, xf, yf = map(int, input().split())
N = int(input())
rects = []
for _ in range(N):
    x1, x2, y1, y2 = map(int, input().split())
    rects.append((x1, x2, y1, y2))
def inside(x, y):
    for x1, x2, y1, y2 in rects:
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
    return False
vis = set()
q = deque()
q.append((xi, yi))
vis.add((xi, yi))
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.popleft()
    if (x, y) == (xf, yf):
        print(1)
        break
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in vis and not inside(nx, ny):
            vis.add((nx, ny))
            q.append((nx, ny))
else:
    print(0)
