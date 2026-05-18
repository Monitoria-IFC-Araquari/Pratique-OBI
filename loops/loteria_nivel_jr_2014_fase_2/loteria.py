L = list(map(int, input().split()))
F = list(map(int, input().split()))

acertos = 0

for i in range(len(F)):
    if F[i] in L:
        acertos += 1

if acertos == 6:
    print("sena")
elif acertos == 5:
    print("quina")
elif acertos == 4:
    print("quadra")
elif acertos == 3:
    print("terno")
else:
    print("azar")
