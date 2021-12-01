a=0
g=0
d=0
while(1):
    n=int(input())
    if n>4:
        continue
    elif n==1:
        a+=1
    elif n==2:
        g+=1
    elif n==3:
        d+=1
    else:
        break
print("MUITO OBRIGADO")
print("Alcool: {}".format(a))
print("Gasolina: {}".format(g))
print("Diesel: {}".format(d))
    
        