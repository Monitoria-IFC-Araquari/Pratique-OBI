n = int(input())
s = [input().strip() for _ in range(n)]

for k in range(n):
    ok = True
    for a in range(k):
        for b in range(a, k):
            concat = s[a] + s[b]
            if s[k] in concat:
                ok = False
                break
            if a != b:
                concat2 = s[b] + s[a]
                if s[k] in concat2:
                    ok = False
                    break
        if not ok:
            break
    if not ok:
        print(s[k])
        break
else:
    print('ok')
