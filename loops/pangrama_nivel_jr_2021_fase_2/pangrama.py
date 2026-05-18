alfabeto = set('abcdefghijlmnopqrstuvxz')
F = input()

letras_encontradas = set()
for C in F:
    if C.isalpha():
        letras_encontradas.add(C)

if len(letras_encontradas) == len(alfabeto):
    print("S")
else:
    print("N")
