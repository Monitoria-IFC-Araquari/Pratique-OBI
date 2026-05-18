n = int(input())
lista = input().split()
P = int(input())
M = int(input())
qtdP = 0
qtdM = 0

for i in range(n):
    if(lista[i] == '1'):
        qtdP += 1
    else:
        qtdM += 1

if qtdP == P and M == qtdM:
    print("S")
else:
    print("N")
