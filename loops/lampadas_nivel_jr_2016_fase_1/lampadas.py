L = int(input())
N = list(map(int, input().split()))
lig1 = False
lig2 = False

for i in range(L):
    if(N[i] == 1):
        lig1 = not lig1
    else:
        lig1 = not lig1
        lig2 = not lig2

if lig1:
    print(1)
else:
    print(0)

if lig2:
    print(1)
else:
    print(0)