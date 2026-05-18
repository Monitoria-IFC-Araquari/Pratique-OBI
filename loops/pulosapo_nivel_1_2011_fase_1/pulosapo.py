N, M = map(int, input().split())
pedras = [0] * N
for _ in range(M):
    P, D = map(int, input().split())
    P -= 1
    for i in range(P, N, D):
        pedras[i] = 1
    for i in range(P, -1, -D):
        pedras[i] = 1
print(' '.join(map(str, pedras)))
