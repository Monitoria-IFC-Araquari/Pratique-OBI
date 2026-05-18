M = int(input())
I1 = int(input())
I2 = int(input())
I3 = M-I1-I2

if I1 >= I3 and I1 >= I2:
    print(I1)
elif I2 >= I3 and I2 >= I1:
    print(I2)
else:
    print(I3)
