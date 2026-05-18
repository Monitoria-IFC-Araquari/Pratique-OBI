def solve():
    n = int(input())
    recebidas = {}
    pendentes = {}
    total = {}
    eventos = []
    for _ in range(n):
        partes = input().strip().split()
        t = partes[0]
        x = int(partes[1])
        eventos.append((t, x))

    tempo_atual = 0
    for i in range(n):
        t, x = eventos[i]
        if t == 'T':
            tempo_atual += x - 1
        elif t == 'R':
            tempo_atual += 1
            if x not in recebidas:
                recebidas[x] = 0
            pendentes[x] = tempo_atual
        elif t == 'E':
            tempo_atual += 1
            if x in pendentes:
                resposta = tempo_atual - pendentes[x]
                recebidas[x] = recebidas.get(x, 0) + resposta
                del pendentes[x]

    for amigo in sorted(set(list(recebidas.keys()) + list(pendentes.keys()))):
        if amigo in pendentes:
            print(amigo, -1)
        else:
            print(amigo, recebidas[amigo])

if __name__ == '__main__':
    solve()
