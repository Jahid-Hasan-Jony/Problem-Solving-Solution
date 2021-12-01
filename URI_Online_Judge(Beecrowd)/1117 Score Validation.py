d=0
c=0
while 1:
    a=float(input())
    if a>=0 and a<=10:
        c+=a
        d+=1
    else:
        print("nota invalida")
    if d==2:
        print("media = {:.2f}".format(c/2))
        break

    
      