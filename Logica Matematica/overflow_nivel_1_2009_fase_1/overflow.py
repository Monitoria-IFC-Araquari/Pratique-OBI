n = int(input())
p, op, q = input().split()
p, q = int(p), int(q)
res = p + q if op == '+' else p * q
print('OVERFLOW' if res > n else 'OK')
