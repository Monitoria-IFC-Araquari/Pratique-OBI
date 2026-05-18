import heapq

C, N = map(int, input().split())
caixas = [0] * C
heapq.heapify(caixas)
esperaram = 0
for _ in range(N):
    T, D = map(int, input().split())
    livre = heapq.heappop(caixas)
    inicio = max(T, livre)
    if inicio - T > 20:
        esperaram += 1
    heapq.heappush(caixas, inicio + D)
print(esperaram)
