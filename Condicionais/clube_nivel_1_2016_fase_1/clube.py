N = int(input())
A, B, C, D, E, F, G = map(int, input().split())
if A + B + C - D - E - F + G > N:
    print('S')
else:
    print('N')
