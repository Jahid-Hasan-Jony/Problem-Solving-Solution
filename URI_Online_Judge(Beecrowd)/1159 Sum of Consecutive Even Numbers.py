while 1:
    x=int(input())
    a=0
    if x==0:
        break
    for i in range(5):
        if x%2==1:
            x+=1
        while x%2==0:
            a+=x
            x+=1
    print(a)