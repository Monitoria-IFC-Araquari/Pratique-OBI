# Entrada
N = int(input()) 
s = input().strip()  

for i in range(N):
    L = int(input()) 

    if L == 1:
        if s == 'A':
            s = 'B'
        elif s == 'B':
            s = 'A'

    elif L == 2:
        if s == 'B':
            s = 'C'
        elif s == 'C':
            s = 'B'

    elif L == 3:
        if s == 'A':
            s = 'C'
        elif s == 'C':
            s = 'A'

print(s)
