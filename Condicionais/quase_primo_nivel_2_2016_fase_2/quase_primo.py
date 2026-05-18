N, K = map(int, input().split())
primes = list(map(int, input().split()))
ans = 0
def dfs(idx, prod, cnt):
    global ans
    if idx == K:
        if cnt:
            if cnt % 2:
                ans += N // prod
            else:
                ans -= N // prod
        return
    dfs(idx + 1, prod, cnt)
    if prod <= N // primes[idx]:
        dfs(idx + 1, prod * primes[idx], cnt + 1)
dfs(0, 1, 0)
print(N - ans)
