S, T, P = map(int, input().split())
alt = list(map(int, input().split()))
adj = [[] for _ in range(S)]
for _ in range(T):
    I, J = map(int, input().split())
    I -= 1
    J -= 1
    if alt[I] > alt[J]:
        adj[I].append(J)
    elif alt[J] > alt[I]:
        adj[J].append(I)
P -= 1
visited = [False] * S
visited[P] = True
stack = [P]
count = -1
while stack:
    v = stack.pop()
    count += 1
    for u in adj[v]:
        if not visited[u]:
            visited[u] = True
            stack.append(u)
print(count)
