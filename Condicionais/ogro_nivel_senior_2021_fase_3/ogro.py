n = int(input())
if n <= 5:
    print('I' * n if n > 0 else '*')
    print('*')
else:
    print('IIIII')
    print('I' * (n - 5))
