X,Y = [float(x) for x in input().split()]
m = [0.0,4.00,4.50,5.00,2.00,1.50]
n = m[int(X)]
j = n*Y
print("Total: R$ %0.2f"%j)