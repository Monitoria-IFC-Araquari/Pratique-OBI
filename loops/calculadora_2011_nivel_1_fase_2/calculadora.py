from fractions import Fraction
n = int(input())
val = Fraction(1, 1)
for _ in range(n):
    d, op = input().split()
    d = int(d)
    if op == '*':
        val *= d
    else:
        val /= d
print(val.numerator if val.denominator == 1 else f'{val.numerator}/{val.denominator}')
