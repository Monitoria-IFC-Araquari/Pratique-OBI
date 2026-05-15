CV, CE, CS, FV, FE, FS = list(map(int, input().split()))

pontos_C = CV * 3 + CE
pontos_F = FV * 3 + FE

if pontos_C > pontos_F:
    print('C')
elif pontos_C < pontos_F:
    print('F')
else:
    if CS > FS:
        print('C')
    elif CS < FS:
        print('F')
    else:
        print('=')