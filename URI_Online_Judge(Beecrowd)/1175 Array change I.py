X=[]
for i in range(20):
    b=int(input())
    X.append(b)
X.reverse()
for i in range(20):
    print("N[{}] = {}".format(i,X[i]))
