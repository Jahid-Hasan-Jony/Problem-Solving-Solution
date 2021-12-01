m=int(input())
n=int(input())
x=0
if m==n:
    x=0
elif m>n:
    m-=1
    for i in range(m,n,-1):
        if i%2==1:
            x+=i     
else:
    m-=1
    for i in range(m,n):
        if i%2==1:
            x+=i
print(x)