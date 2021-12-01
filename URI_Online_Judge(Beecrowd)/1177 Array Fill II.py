T=int(input())
A=[]
for t in range(1000):
    for i in range(T):
        A.append(i)
    print("N[{}] = {}".format(t,A[t]))
        