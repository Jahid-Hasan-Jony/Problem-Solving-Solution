a,b=map(int,input().split())
q=a//b
r=a-(b*q)
if r<0:
    q=0
    r=0
    q=a//b+1
    r=a-(b*q)
print(q,r)
    

