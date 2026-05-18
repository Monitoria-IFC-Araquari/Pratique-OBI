N, K = map(int, input().split())
X = list(map(int, input().split()))
pref = 0
cnt = {0: 1}
ans = 0
for x in X:
    pref += x
    ans += cnt.get(pref - K, 0)
    cnt[pref] = cnt.get(pref, 0) + 1
print(ans)
