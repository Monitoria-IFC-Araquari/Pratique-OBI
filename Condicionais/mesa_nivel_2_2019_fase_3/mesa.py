a = int(input())
b = int(input())

ana = a % 3
beatriz = b % 3
if beatriz == ana:
    beatriz = (beatriz + 1) % 3
carolina = 3 - ana - beatriz

print(carolina)
