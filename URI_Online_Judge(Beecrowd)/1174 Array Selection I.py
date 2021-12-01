X=[]
for i in range(100):
    b=float(input())
    X.append(b)
    if b<=10:
        print("A[{}] = {:0.1f}".format(i,X[i]))
