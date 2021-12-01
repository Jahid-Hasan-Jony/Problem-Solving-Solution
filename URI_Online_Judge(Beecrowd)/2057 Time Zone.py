a,b,c=map(int,input().split())
n=a+b+c
if n==0:
    print(n)
if n<24 and n>0:
    print(n)
if n>=24:
    n=n-24
    print(n)
if n<0:
    n=24+n
    print(n)
