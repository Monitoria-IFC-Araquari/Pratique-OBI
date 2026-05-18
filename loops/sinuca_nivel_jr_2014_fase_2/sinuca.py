N = int(input())
S = list(map(int, input().split()))
sinuca = [S]
contador = 0

for i in range(N):
    linha = []
    for j in range(N):
        if j == N-contador-1:
            break
        if sinuca[i][j] == sinuca[i][j + 1]:
            linha.append(1)
        else: 
            linha.append(-1)  
    contador += 1
    sinuca.append(linha)

if sinuca[N-1][0] == 1:
    print("preta")
else:
    print("branca")

