t1 = int(input())
t2 = int(input())
t3 = int(input())
times = [(t1, 1), (t2, 2), (t3, 3)]
times.sort()
for _, n in times:
    print(n)
