MOD = 10**9 + 7

states = []
for a in range(3):
    for b in range(3):
        if a == b:
            continue
        for c in range(3):
            if b == c:
                continue
            states.append((a, b, c))

k = len(states)
T = [[0] * k for _ in range(k)]
for i, (a, b, c) in enumerate(states):
    for j, (x, y, z) in enumerate(states):
        if a != x and b != y and c != z:
            T[i][j] = 1

def mat_mul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for k_ in range(n):
            aik = Ai[k_]
            if aik:
                Bk = B[k_]
                for j in range(n):
                    Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
    return C

def mat_pow(M, e):
    n = len(M)
    R = [[0] * n for _ in range(n)]
    for i in range(n):
        R[i][i] = 1
    while e:
        if e & 1:
            R = mat_mul(R, M)
        M = mat_mul(M, M)
        e >>= 1
    return R

n = int(input())
if n == 1:
    print(k % MOD)
else:
    P = mat_pow(T, n - 1)
    total = 0
    for row in P:
        total = (total + sum(row)) % MOD
    print(total)
