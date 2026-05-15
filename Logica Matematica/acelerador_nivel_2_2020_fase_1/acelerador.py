km = int(input())

posicao = (3 + km) % 8

sensor = (posicao + 2) % 3 + 1

print(sensor)

