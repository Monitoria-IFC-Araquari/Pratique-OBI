def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])
    m = 1 << n
    skills = list(map(int, data[2:2 + m]))
    j = skills[0]
    w = sum(1 for h in skills[1:] if h < j)
    s = sum(1 for h in skills[1:] if h > j)
    MOD = 1000000007
    fact = [1]
    for i in range(1, m + 1):
        fact.append(fact[-1] * i % MOD)

    def perm(a, b):
        if b > a:
            return 0
        return fact[a] * pow(fact[a - b], MOD - 2, MOD) % MOD

    if k == n + 1:
        if s > 0:
            print(0)
        else:
            print(fact[m])
        return

    need_w = (1 << (k - 1)) - 1
    need_set_k = 1 << (k - 1)
    if w < need_w or s < 1:
        print(0)
        return

    ways1 = perm(w, need_w)
    w_rem = w - need_w
    total_rem = w_rem + s
    if total_rem < need_set_k:
        print(0)
        return
    ways2 = (perm(total_rem, need_set_k) - perm(w_rem, need_set_k)) % MOD
    remaining = m - 1 - need_w - need_set_k
    ways3 = fact[remaining]
    ans = m * ways1 % MOD * ways2 % MOD * ways3 % MOD
    print(ans % MOD)

if __name__ == '__main__':
    solve()
