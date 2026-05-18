R = int(input())
campo = [0]
novoarr = []
i = 0

while i < R + 1:
    i += 1
    if i == R + 1:
        campo.append(0)
        break
    T = int(input())
    campo.append(T)

for i in range(1, len(campo) - 1):
    contador = 0
    if campo[i + 1] == 1:
        contador += 1
    if campo[i - 1] == 1:
        contador += 1
    novocampo = campo[i] + contador
    novoarr.append(novocampo)
    contador = 0

for i in range(len(novoarr)):
    print(novoarr[i]) 
