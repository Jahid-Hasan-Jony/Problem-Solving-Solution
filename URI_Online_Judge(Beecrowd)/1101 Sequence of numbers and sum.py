for i in range(0,100):
    Sum=0
    x,y=[int(m) for m in input().split()]
    if x<=0 or y<=0:
        break
    if x>y:
        y-=1
        for i in range(y,x):
            i+=1
            print(i,end=" ")
            Sum+=i
        print("Sum={}".format(Sum))
    elif x==y:
        print(x,"Sum={}".format(x))
    else:
        x-=1
        for i in range(x,y):
            i+=1
            print(i,end=" ")
            Sum+=i
        print("Sum={}".format(Sum))
