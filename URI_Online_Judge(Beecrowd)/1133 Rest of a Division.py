x=int(input())
y=int(input())
if x<y:
    x+=1
    for i in range(x,y):
        if i%5==2 or i%5==3:
            print(i)
else:
    y+=1
    for i in range(y,x):
        if i%5==2 or i%5==3:
            print(i)
