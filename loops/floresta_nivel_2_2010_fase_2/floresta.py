N = int(input())
count = 0
y = 2
while True:
    num = N - 1 + y
    den = 2 * y - 1
    if den > num:
        break
    if num % den == 0:
        x = num // den
        if x >= y:
            count += 1
    y += 1
print(count)
