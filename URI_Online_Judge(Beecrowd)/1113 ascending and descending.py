while 1:
    x,y=[int(m) for m in input().split()]
    if x==y:
        break
    elif x>y:
        print("Decrescente")
    else:
        print("Crescente")
