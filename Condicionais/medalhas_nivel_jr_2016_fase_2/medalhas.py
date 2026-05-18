T1 = int(input())
T2 = int(input())
T3 = int(input())

if T1 < T2 and T1 < T3:
    if T2 < T3:
        print(1, 2, 3)
    else:
        print(1, 3, 2)
elif T2 < T1 and T2 < T3:
    if T1 < T3:
        print(2, 1, 3)
    else:
        print(3, 1, 2)
elif T3 < T1 and T3 < T2:
    if T1 < T2:
        print(2, 3, 1)
    else:
        print(3, 2, 1)