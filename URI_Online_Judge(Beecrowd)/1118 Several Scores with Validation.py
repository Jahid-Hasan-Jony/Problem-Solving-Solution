while 1:
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
            break
    print("media = {:.2f}".format(c/2))
    while 1:
        n=float(input())
        print("novo calculo (1-sim 2-nao)")
        if n==1 or n==2:
            break
    if n==1:
        continue
    else:
        break
