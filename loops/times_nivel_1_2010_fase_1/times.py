def solve():
    n, t = map(int, input().split())
    alunos = []
    for _ in range(n):
        nome, habilidade = input().strip().split()
        habilidade = int(habilidade)
        alunos.append((habilidade, nome))
    alunos.sort(key=lambda x: (-x[0], x[1]))
    times = [[] for _ in range(t)]
    for i, (hab, nome) in enumerate(alunos):
        times[i % t].append(nome)
    for i in range(t):
        print(f'Time {i + 1}')
        for nome in sorted(times[i]):
            print(nome)
        print()

if __name__ == '__main__':
    solve()
