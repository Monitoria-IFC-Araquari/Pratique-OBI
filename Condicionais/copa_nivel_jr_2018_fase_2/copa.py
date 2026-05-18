K = int(input())
L = int(input())

if (K - 1) // 2 == (L - 1) // 2:
    print("oitavas")
elif(K - 1) // 4 == (L - 1) // 4:
    print("quartas")
elif (K - 1) // 8 == (L - 1) // 8:
    print("semifinal")
else:
    print("Final")