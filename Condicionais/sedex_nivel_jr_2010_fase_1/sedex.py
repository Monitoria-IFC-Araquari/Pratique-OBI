D = int(input())
A, L, P = list(map(int, input().split()))

if A < D or L < D or P < D:
    print('N')
else: 
    print('S')