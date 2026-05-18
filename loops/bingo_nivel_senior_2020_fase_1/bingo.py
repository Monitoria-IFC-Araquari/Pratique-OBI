n, k, u = map(int, input().split())
cartelas = [set(map(int, input().split())) for _ in range(n)]
sorteio = list(map(int, input().split()))

acertos = [0] * n
vencedoras = []
melhor_tempo = None

for tempo, num in enumerate(sorteio):
    for i in range(n):
        if num in cartelas[i]:
            acertos[i] += 1
            if acertos[i] == k:
                if melhor_tempo is None or tempo < melhor_tempo:
                    melhor_tempo = tempo
                    vencedoras = [i + 1]
                elif tempo == melhor_tempo:
                    vencedoras.append(i + 1)
    if melhor_tempo is not None and tempo > melhor_tempo:
        break

print(' '.join(map(str, sorted(vencedoras))))
