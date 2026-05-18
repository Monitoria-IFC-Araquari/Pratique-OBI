import sys
sys.setrecursionlimit(20000)

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]
navios = [[0] * M for _ in range(N)]
navio_id = 0
tamanhos = []

def dfs(i, j, nid):
    stack = [(i, j)]
    count = 0
    while stack:
        x, y = stack.pop()
        if x < 0 or x >= N or y < 0 or y >= M or grid[x][y] != '#':
            continue
        grid[x][y] = '.'
        navios[x][y] = nid
        count += 1
        stack.append((x - 1, y))
        stack.append((x + 1, y))
        stack.append((x, y - 1))
        stack.append((x, y + 1))
    return count

for i in range(N):
    for j in range(M):
        if grid[i][j] == '#':
            navio_id += 1
            tam = dfs(i, j, navio_id)
            tamanhos.append(tam)

acertos = [0] * (navio_id + 1)
K = int(input())
for _ in range(K):
    L, C = map(int, input().split())
    nid = navios[L - 1][C - 1]
    if nid > 0:
        acertos[nid] += 1

destruidos = sum(1 for i in range(1, navio_id + 1) if acertos[i] == tamanhos[i - 1])
print(destruidos)
