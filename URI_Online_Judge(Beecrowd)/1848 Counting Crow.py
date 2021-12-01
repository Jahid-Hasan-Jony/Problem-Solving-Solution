a=0
b=0
c=0
d=0
e=0
f=0
l=0
g=0
h=0
while l!=3:
    n=input()
    if n=="***":
        a+=7
    if n=="--*":
        b+=1
    if n=="-**":
        c+=3
    if n=="*--":
        d+=4
    if n=="*-*":
        e+=5
    if n=="**-":
        h+=6
    if n=="-*-":
        f+=2
    if n=="---":
        g+=0
    if n=="caw caw":
        print(a+b+c+d+e+f+g+h)
        l+=1
        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        h=0
        g=0
    
       
        