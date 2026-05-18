n = int(input())
count = 0
for _ in range(n):
    line = input()
    for c in line:
        if c == '{':
            count += 1
        elif c == '}':
            count -= 1
            if count < 0:
                print('N')
                exit()
print('S' if count == 0 else 'N')
