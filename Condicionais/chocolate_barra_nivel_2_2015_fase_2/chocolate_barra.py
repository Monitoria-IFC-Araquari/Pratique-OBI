n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
metade = n // 2
if (x1 <= metade and x2 > metade) or (x1 > metade and x2 <= metade):
    print('S')
elif (y1 <= metade and y2 > metade) or (y1 > metade and y2 <= metade):
    print('S')
else:
    print('N')
