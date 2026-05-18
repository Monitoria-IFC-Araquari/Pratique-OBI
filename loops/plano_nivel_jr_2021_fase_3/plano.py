M = int(input())
N = int(input())
vagas_d = [int(input()) for _ in range(N)]
vagas_pegas = []

for i in range(N):
    if vagas_d[i] not in vagas_pegas:
        vagas_pegas.append(vagas_d[i])

print(len(vagas_pegas))
