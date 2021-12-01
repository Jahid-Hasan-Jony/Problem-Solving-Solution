A,B,C,D = [int(x) for x in input().split()]
if B > C and D > A and C + D > A + B:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")