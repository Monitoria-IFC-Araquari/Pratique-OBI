N, D = map(int, input().split())
C = list(map(int, input().split()))
C2 = C + C
s = 0
j = 0
for i in range(2 * N):
    while j < 2 * N and s < D:
        s += C2[j]
        j += 1
    if s == D:
        print('S')
        break
    s -= C2[i]
else:
    print('N')
