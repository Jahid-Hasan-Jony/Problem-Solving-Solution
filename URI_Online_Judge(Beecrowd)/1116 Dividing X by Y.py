a=int(input())
for i in range(a):
    x, y = [int(x) for x in input().split()]
    if y==0:
        print("divisao impossivel")
    else:
        r=x/y
        print("%0.1f"%r)