n=int(input())
for i in range(n):
    a=0
    x=int(input())
    for i in range(1,x+1):
        if x%i==0:
            a+=i
    if a==x+1:
        print("{} eh primo".format(x))
    else:
        print("{} nao eh primo".format(x))