A = int(input())
x = A
y = A
tabuleiro = []

for i in range(A):
    C = list(map(int, input().split()))
    tabuleiro.append(C)

for i in range(1, A):
    for j in range(1, A):
        branco = 0
        preto = 0

        if tabuleiro[i - 1][j - 1] == 0:
            branco += 1
        else:
            preto += 1

        if tabuleiro[i - 1][j] == 0:
            branco += 1
        else:
            preto += 1
        
        if tabuleiro[i][j-1] == 0:
            branco += 1
        else:
            preto += 1

        if preto > branco:
            tabuleiro[i][j] = 0
        else:
            tabuleiro[i][j] = 1

        preto = 0
        branco = 0

print(tabuleiro[A -1][A - 1])