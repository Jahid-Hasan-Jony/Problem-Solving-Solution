n=int(input())
for i in range(n):
    a=0
    x,y=[int(i) for i in input().split()]
    for i in range(y):
        if x%2==0:
            x+=1
        while x%2==1:
            a+=x
            x+=1
    print(a)
