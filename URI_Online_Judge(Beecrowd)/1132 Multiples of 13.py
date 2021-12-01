x=int(input())
y=int(input())
n=0
if x<y:
    y+=1
    for i in range(x,y):
        if i%13!=0:
            n+=i
else:
    x+=1
    for i in range(y,x):
        if i%13!=0:
            n+=i
print(n)