s = input().strip()
naipes = {'C': 0, 'E': 1, 'U': 2, 'P': 3}
presentes = [set() for _ in range(4)]
duplicado = [False] * 4

for i in range(0, len(s), 3):
    num = int(s[i:i+2])
    naipe = naipes[s[i+2]]
    if num in presentes[naipe]:
        duplicado[naipe] = True
    presentes[naipe].add(num)

for i in range(4):
    if duplicado[i]:
        print("erro")
    else:
        print(13 - len(presentes[i]))
