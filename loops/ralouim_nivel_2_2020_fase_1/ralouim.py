p = int(input())
posicoes = []
gulomax = 0
i = -1

for i in range(p):
    X, Y = map(int, input().split())
    posicoes.append([X, Y])


posicoes.sort(reverse=True)

if(posicoes[0][0] > 0 or posicoes[0][1] > 0 ):
    gulomax += 1
    for i in range(len(posicoes)-1):
        if(posicoes[i][0] > posicoes[i+1][0] and posicoes[i][1] > posicoes[i+1][1]):
            gulomax += 1
        elif (posicoes[i][0] > posicoes[i+1][0] and posicoes[i][1] == posicoes[i+1][1]):
            gulomax += 1
        elif posicoes[i][0] == posicoes[i+1][0] and posicoes[i][1] > posicoes[i+1][1]:
            gulomax += 1
else:
    gulomax = 0

print(gulomax)