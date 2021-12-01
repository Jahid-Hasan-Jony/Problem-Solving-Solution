X=[]

b=int(input())
X.append(b)
print("N[{}] = {}".format(0,X[0]))
for i in range(1,10):
    b=b*2
    X.append(b)
    print("N[{}] = {}".format(i,X[i]))