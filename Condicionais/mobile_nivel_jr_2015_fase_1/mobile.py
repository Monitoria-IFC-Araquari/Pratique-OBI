A = int(input())
B = int(input())
C = int(input())
D = int(input())

if ((B + C + D) == A) and ((B + C) == D) and B == C:
    print('S')
else:
    print('N')

