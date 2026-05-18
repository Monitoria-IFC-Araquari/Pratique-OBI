N, C, S = list(map(int, input().split()))
A = list(map(int, input().split()))

vzs = 0
est = 1

if est == S:
    vzs += 1 

for i in range(len(A)):
        if A[i] == 1:
            est += 1
        elif A[i] == -1:
            est -= 1
    
        if est > N:
            est = 1
        elif est < 1:
            est = N
        
        if est == S:
            vzs += 1

print(vzs)