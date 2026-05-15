A = int(input())
B = int(input())
C = int(input())

if (A + B < C or C > B and B > A):
    print(1)
elif(A < B and A < C or B < C):
    print(2)
else:
    print(3)
