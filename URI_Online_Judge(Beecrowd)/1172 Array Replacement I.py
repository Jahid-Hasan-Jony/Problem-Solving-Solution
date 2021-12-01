X=[]
for i in range(10):
    b=int(input())
    if b<=0:
        X.append(1)
    else:
        X.append(b)
for i in range(10):
    print("X[{}] = {}".format(i,X[i]))