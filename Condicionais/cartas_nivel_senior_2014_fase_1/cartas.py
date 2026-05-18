v = list(map(int, input().split()))
if all(v[i] < v[i+1] for i in range(4)):
    print('C')
elif all(v[i] > v[i+1] for i in range(4)):
    print('D')
else:
    print('N')
