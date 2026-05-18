V, D = map(int, input().split())
M = list(map(int, input().split()))

msg = "S"

for i in range(1, V):
    distancia_max = M[i] - M[i-1]   

    if not distancia_max <= D:
        msg = "N"
        break

print(msg)