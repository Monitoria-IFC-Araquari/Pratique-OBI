M = int(input())
N = int(input())
i = 0
j = 0
xadrez = []

while i < M:
    i += 1
    linha = []
    while j < N:
        j += 1
        if (j + i) % 2 == 0:
            xadrez.append(1)
        else: 
            xadrez.append(0)
    j = 0    

print(xadrez[len(xadrez) - 1])