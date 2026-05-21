N, C, M = map(int, input().split())

carimbadas = list(map(int, input().split()))
compradas = list(map(int, input().split()))

faltam = 0

for figurinha in carimbadas:
    if figurinha not in compradas:
        faltam += 1

print(faltam)