f=[0,1]
for i in range(59):
    a=(f[-2]+f[-1])
    f.append(a)
x=int(input())
for i in range(x):
    x=int(input())
    print("Fib({}) = {}".format(x,f[x]))
    
