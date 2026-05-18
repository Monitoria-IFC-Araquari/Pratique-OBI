N = int(input())
C = list(map(int, input().split()))

qtd = 0

for i in range(N):
    if C[i] == 1 and C[i + 1] == 0 and C[i + 2] == 0:
        qtd += 1
    if i == N - 3:
        break
print(qtd)