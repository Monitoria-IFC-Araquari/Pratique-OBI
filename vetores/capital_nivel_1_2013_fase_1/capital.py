a = list(map(int, input().split()))
a.sort()
print('S' if a[0] * a[3] == a[1] * a[2] else 'N')
