a = input().strip()
b = input().strip()
m = max(len(a), len(b))
a = a.zfill(m)
b = b.zfill(m)

ra, rb = '', ''
for da, db in zip(a, b):
    if da > db:
        ra += da
    elif db > da:
        rb += db
    else:
        ra += da
        rb += db

ra = ra.lstrip('0') or '0'
rb = rb.lstrip('0') or '0'
if not ra:
    ra = '-1'
if not rb:
    rb = '-1'
x, y = (ra, rb) if ra <= rb else (rb, ra)
print(x, y)
