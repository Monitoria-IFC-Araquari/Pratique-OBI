a1, b1, a2, b2, a, b = map(int, input().split())

def can_alone(r):
    return (r[0] == a and r[1] == b) or (r[0] == b and r[1] == a)

def fits(r1, r2):
    if can_alone(r1) or can_alone(r2):
        return True
    for (w1, h1) in [r1, (r1[1], r1[0])]:
        for (w2, h2) in [r2, (r2[1], r2[0])]:
            if w1 == w2 and h1 + h2 == b and w1 == a:
                return True
            if w1 == w2 and h1 + h2 == a and w1 == b:
                return True
            if h1 == h2 and w1 + w2 == a and h1 == b:
                return True
            if h1 == h2 and w1 + w2 == b and h1 == a:
                return True
            mw = min(w1, w2)
            if mw >= a and h1 + h2 >= b:
                return True
            if mw >= b and h1 + h2 >= a:
                return True
            mh = min(h1, h2)
            if w1 + w2 >= a and mh >= b:
                return True
            if w1 + w2 >= b and mh >= a:
                return True
    return False

print('S' if fits((a1, b1), (a2, b2)) else 'N')
