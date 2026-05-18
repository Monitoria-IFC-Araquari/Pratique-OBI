N = int(input())
F = int(input())
figurinhas = []


for i in range(F):
    figurinha = int(input())

    if figurinha not in figurinhas:
        figurinhas.append(figurinha)

print(N - len(figurinhas))
