n=int(input())
o=0
for i in range(n):
    x,y=[int(m) for m in input().split()]
    if x==y:
        print(0)
    elif x>y:
        x-=1
        if x==y:
            print(0)
        else:    
            for i in range(x,y,-1):
               if i%2==1:
                   o+=i
            print(o)
        o=o-o
    else:
        x+=1
        if y==x:
            print(0)
        else:
            for i in range(x,y):
               if i%2==1:
                   o+=i
            print(o)
        o=o-o
       
