R = int(input())
F = int(input())
C = int(input())

if(F > (R * 3) or C < 95):
    print("diminuir")
elif(F < (R * 2) and C > 97):
    print("aumentar")
else:
    print("manter")
