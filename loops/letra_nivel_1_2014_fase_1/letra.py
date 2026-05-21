letra = input()
texto = input()

palavras = texto.split()

total = len(palavras)
cont = 0

for palavra in palavras:
    if letra in palavra:
        cont += 1

porcentagem = (cont / total) * 100

print(f"{porcentagem:.1f}")