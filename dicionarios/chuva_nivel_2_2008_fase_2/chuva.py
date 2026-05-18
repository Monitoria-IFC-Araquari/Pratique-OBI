from heapq import heappush, heappop
from bisect import bisect_left

xi, yi, xf, yf = map(int, input().split())
n = int(input())
rects = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    rects.append((x1, y1, x2, y2))

corners = []
pts_set = {(xi, yi), (xf, yf)}
for x1, y1, x2, y2 in rects:
    for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
        pts_set.add(p)
        corners.append(p)
    if y1 <= yi <= y2:
        pts_set.add((x1, yi))
        pts_set.add((x2, yi))
    if x1 <= xi <= x2:
        pts_set.add((xi, y1))
        pts_set.add((xi, y2))
    if y1 <= yf <= y2:
        pts_set.add((x1, yf))
        pts_set.add((x2, yf))
    if x1 <= xf <= x2:
        pts_set.add((xf, y1))
        pts_set.add((xf, y2))

col_x = {}
for vx, vy in pts_set:
    col_x.setdefault(vx, []).append(vy)
col_y = {}
for vx, vy in pts_set:
    col_y.setdefault(vy, []).append(vx)

pre_x = {}
for xval in col_x:
    intervals = []
    for rx1, ry1, rx2, ry2 in rects:
        if rx1 <= xval <= rx2:
            intervals.append((ry1, ry2))
    if intervals:
        intervals.sort()
        merged = []
        cs, ce = intervals[0]
        for s, e in intervals[1:]:
            if s > ce:
                merged.append((cs, ce))
                cs, ce = s, e
            else:
                ce = max(ce, e)
        merged.append((cs, ce))
        pre_x[xval] = merged
    else:
        pre_x[xval] = []

pre_y = {}
for yval in col_y:
    intervals = []
    for rx1, ry1, rx2, ry2 in rects:
        if ry1 <= yval <= ry2:
            intervals.append((rx1, rx2))
    if intervals:
        intervals.sort()
        merged = []
        cs, ce = intervals[0]
        for s, e in intervals[1:]:
            if s > ce:
                merged.append((cs, ce))
                cs, ce = s, e
            else:
                ce = max(ce, e)
        merged.append((cs, ce))
        pre_y[yval] = merged
    else:
        pre_y[yval] = []

def covered_len(pre, lo, hi):
    if not pre:
        return 0
    i = bisect_left(pre, (lo, -10**18))
    cov = 0
    while i < len(pre) and pre[i][0] < hi:
        cs, ce = pre[i]
        cov += min(ce, hi) - max(cs, lo)
        i += 1
    return cov

corner_set = set(corners)
dist = {}
dist[(xi, yi)] = 0
pq = [(0, xi, yi)]
while pq:
    d, x, y = heappop(pq)
    if d != dist.get((x, y), 10**18):
        continue
    if (x, y) == (xf, yf):
        print(d)
        break
    for vy in col_x.get(x, []):
        if vy == y:
            continue
        lo, hi = (y, vy) if y < vy else (vy, y)
        nd = d + hi - lo - covered_len(pre_x.get(x, []), lo, hi)
        if nd < dist.get((x, vy), 10**18):
            dist[(x, vy)] = nd
            heappush(pq, (nd, x, vy))
    for vx in col_y.get(y, []):
        if vx == x:
            continue
        lo, hi = (x, vx) if x < vx else (vx, x)
        nd = d + hi - lo - covered_len(pre_y.get(y, []), lo, hi)
        if nd < dist.get((vx, y), 10**18):
            dist[(vx, y)] = nd
            heappush(pq, (nd, vx, y))
    if x == xf:
        lo, hi = (y, yf) if y < yf else (yf, y)
        nd = d + hi - lo - covered_len(pre_x.get(x, []), lo, hi)
        if nd < dist.get((xf, yf), 10**18):
            dist[(xf, yf)] = nd
            heappush(pq, (nd, xf, yf))
    elif y == yf:
        lo, hi = (x, xf) if x < xf else (xf, x)
        nd = d + hi - lo - covered_len(pre_y.get(y, []), lo, hi)
        if nd < dist.get((xf, yf), 10**18):
            dist[(xf, yf)] = nd
            heappush(pq, (nd, xf, yf))
    else:
        nd = d + abs(x - xf) + abs(y - yf)
        if nd < dist.get((xf, yf), 10**18):
            dist[(xf, yf)] = nd
            heappush(pq, (nd, xf, yf))
    if (x, y) not in corner_set:
        for cx, cy in corners:
            nd = d + abs(x - cx) + abs(y - cy)
            if nd < dist.get((cx, cy), 10**18):
                dist[(cx, cy)] = nd
                heappush(pq, (nd, cx, cy))
