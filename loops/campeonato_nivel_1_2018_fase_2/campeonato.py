x = list(map(int, input().split()))
n = len(x)

pos1 = x.index(1)
pos9 = x.index(9)

phase = 0
while (1 << phase) < n:
    g1 = pos1 // (1 << phase)
    g9 = pos9 // (1 << phase)
    if g1 != g9:
        phase += 1
    else:
        break

if (1 << phase) == n:
    print('final')
elif (1 << phase) == (n // 2):
    print('semifinal')
elif (1 << phase) == (n // 4):
    print('quartas')
else:
    print('oitavas')
