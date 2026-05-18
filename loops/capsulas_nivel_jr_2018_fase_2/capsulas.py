N, F = map(int, input().split())
C = list(map(int, input().split()))

soma = 0
i = 0
dias = 1
moedas = 0

while i < N:
    dias += 1
    i += 1

    if dias % C[i] == 0:
        moedas += 1
    if i == N - 1 :
        i = 0
    if dias > F:
        break

print(dias)



