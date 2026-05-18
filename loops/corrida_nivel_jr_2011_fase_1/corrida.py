C, V = map(int, input().split())
voltas = []
melhor = 0

for i in range(C):
    tempo = list(map(int, input().split()))
    soma = 0
    for j in range(len(tempo)):
        soma += tempo[j]
    if i == 0:
        melhor = soma
    if soma < melhor:
        melhor = soma
    voltas.append(soma)
    soma = 0

posicao_melhor = voltas.index(melhor)

print(posicao_melhor + 1)


