M = input()
d = 0
c = 0

for i in range(len(M)):
    if M[i] == '(' and M[i-1] == "-" and M[i-2] == ":":
        c += 1
    elif M[i] == ')' and M[i-1] == "-" and M[i-2] == ":":
        d += 1

if d > c:
    print("divertido")
elif c > d:
    print("chateado")
else:
    print("neutro")
