t=int(input())
for i in range(t):
    n=0
    PA,PB,GA,GB=input().split()
    PA=int(PA)
    PB=int(PB)
    GA=float(GA)
    GB=float(GB)
    while(PA<=PB):
        PA = int(PA + (PA*GA)/100)
        PB = int(PB + (PB*GB)/100)
        n+=1
        if (n>100):
            print("Mais de 1 seculo.")
            break
    if(n<=100):
        print("{} anos.".format(int(n)))
        