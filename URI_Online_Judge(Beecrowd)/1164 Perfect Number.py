n=int(input())
for i in range(n):
    a=0
    x=int(input())
    for i in range(1,x):
        if x%i==0:
            a+=i
    if a==x:
        print("{} eh perfeito".format(x))
    else:
        print("{} nao eh perfeito".format(x))

            
    