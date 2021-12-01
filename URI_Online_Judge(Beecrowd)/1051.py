a=float(input())
b=a-2000
if a<=2000:
    print("Isento")
else:
    if b<=1000:
        c=(b*8)/100
        print("R$ %0.2f"%c)
    elif b<=1500:
        e=(1000*8)/100
        c= b-1000
        d=(c*18)/100
        print("R$ %0.2f"%(d+e))
    elif b>1500:
        c=(1000*8)/100
        d=(1500*18)/100
        e=b-2500
        f=(e*28)/100
        print("R$ %0.2f"%(c+d+f))
        