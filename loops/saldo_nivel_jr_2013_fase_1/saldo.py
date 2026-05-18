N, S = map(int, input().split())
i = 0
saldo_dias = [S]
gasto = S
while i < N:
    i += 1
    A = int(input())
    S += A
    saldo_dias.append(S)

saldo_dias.sort()
print(saldo_dias[0])