m=0
n=0
while 1: 
    a=int(input())
    if a<0:
        break
    else:
        n+=1
        m+=a
    
print("{:.2f}".format(m/n))
        