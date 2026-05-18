f1, f2, f3 = map(int, input().split())
intervals = [(f1, f1 + 200), (f2, f2 + 200), (f3, f3 + 200)]
intervals.sort()
covered = 0
cur_end = 0
for s, e in intervals:
    if s > cur_end:
        covered += e - s
        cur_end = e
    elif e > cur_end:
        covered += e - cur_end
        cur_end = e
print((600 - covered) * 100)
