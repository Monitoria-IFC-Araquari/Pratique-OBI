X, Y = map(int, input().split())
L1, H1 = map(int, input().split())
L2, H2 = map(int, input().split())

def cabe(w1, h1, w2, h2):
    if (w1 + w2 <= X and max(h1, h2) <= Y):
        return True
    if (max(w1, w2) <= X and h1 + h2 <= Y):
        return True
    return False

if (cabe(L1, H1, L2, H2) or cabe(H1, L1, L2, H2) or
    cabe(L1, H1, H2, L2) or cabe(H1, L1, H2, L2)):
    print('S')
else:
    print('N')
