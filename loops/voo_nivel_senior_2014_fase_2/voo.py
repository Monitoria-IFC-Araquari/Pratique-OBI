import sys

def to_min(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

pa, cb, pb, ca = sys.stdin.readline().split()
pa = to_min(pa)
cb = to_min(cb)
pb = to_min(pb)
ca = to_min(ca)

for d in range(-11, 13):
    dur = (cb - pa + d * 60) % (24 * 60)
    if 0 < dur < 12 * 60:
        if (pb + dur) % (24 * 60) == (ca - d * 60) % (24 * 60):
            print(dur, d)
            break
