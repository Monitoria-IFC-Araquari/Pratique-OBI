A,B,C = list(map(int, input().split()))
X,Y,Z = list(map(int, input().split()))

if(A <= X and B <= Y and C <= Z):
    qtd_containers = (X // A) * (Y // B) * (Z // C)
    print(int(qtd_containers))
else:
    print(0)

