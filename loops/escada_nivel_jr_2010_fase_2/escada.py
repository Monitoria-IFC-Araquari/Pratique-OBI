N = int(input())
tempos = []

lig = 10

for i in range(N):
    T = int(input())
    tempos.append(T)

if N == 0:
    print(0)
else: 
    for i in range(1, N):
        intervalo = tempos[i] - tempos[i-1]
        if intervalo < 10:
            lig += intervalo
        else:
            lig += 10
    print(lig)