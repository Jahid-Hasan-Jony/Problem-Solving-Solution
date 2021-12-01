n=int(input())
t=0
for i in range(n):
    a,b=map(int,input().split())
    if a==1001:
        t+=1.50*b
    if a==1002:
        t+=2.50*b
    if a==1003:
        t+=3.50*b
    if a==1004:
        t+=4.50*b
    if a==1005:
        t+=5.50*b
print("%.2f"%t)