n=[]
x=float(input())
n.append(x)
print("N[{}] = {:.4f}".format(0,n[0]))
for i in range(1,100):
    a=(n[-1])/2
    n.append(a)
    print("N[{}] = {:.4f}".format(i,n[i]))
    
