import sys

def pontos(a, b):
    s = a + b
    if a == b:
        return 2 * s
    if abs(a - b) == 1:
        return 3 * s
    return s

lia1 = int(sys.stdin.readline())
lia2 = int(sys.stdin.readline())
car1 = int(sys.stdin.readline())
car2 = int(sys.stdin.readline())

pl = pontos(lia1, lia2)
pc = pontos(car1, car2)

if pl > pc:
    print("Lia")
elif pc > pl:
    print("Carolina")
else:
    print("empate")
