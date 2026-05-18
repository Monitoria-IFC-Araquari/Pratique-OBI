n = int(input())
v = [int(input()) for _ in range(n)]

ans = 1
for a in set(v):
    for b in set(v):
        if a > b:
            continue
        last = -1
        cnt = 0
        for x in v:
            if (x == a or x == b) and x != last:
                cnt += 1
                last = x
        if cnt > ans:
            ans = cnt

print(ans)
