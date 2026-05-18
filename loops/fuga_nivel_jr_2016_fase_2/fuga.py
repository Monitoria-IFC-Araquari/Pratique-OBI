H, P, F, D = list(map(int, input().split()))

pos = F

if D == -1: 
    while True:
        pos = (pos - 1) % 16
        print(pos)
        if pos == H:
            print("S")
            break
        if pos == P:
            print("N")
            break
else:  
    while True:
        pos = (pos + 1) % 16
        if pos == H:
            print("S")
            break
        if pos == P:
            print("N")
            break
