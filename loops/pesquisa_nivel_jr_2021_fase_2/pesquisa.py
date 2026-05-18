N = int(input())
estados = []

for i in range(N):
    E, A, G = list(map(str, input().split()))
    vantajoso = float(G) * 0.70
    if float(A) <= vantajoso:
        estados.append(E)

if not estados:
    print('*')
else:
    for i in range(len(estados)):
        print(estados[i])