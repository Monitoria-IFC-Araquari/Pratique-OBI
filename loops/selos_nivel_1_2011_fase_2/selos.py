N = int(input())
if N == 1:
    print('N')
else:
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            print('S')
            break
    else:
        print('N')
