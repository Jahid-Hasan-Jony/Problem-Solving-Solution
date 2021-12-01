import math
while 1:
    n=input().split()
    if n==['0']:
        break
    a,b,c=n
    a,b,c=int(a),int(b),int(c)
    h=math.sqrt(a*b*100/c)
    print(int(h))