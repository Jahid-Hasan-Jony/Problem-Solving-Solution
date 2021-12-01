p,q,r= [float(x) for x in input().split()]
d=[p,q,r]
d.sort(reverse=True)
a=d[0]
b=d[1]
c=d[2]

m= b+c
n= c+a
y= a+b


if a>=m or b>=n or c>=y:
    print("NAO FORMA TRIANGULO")
else:
    if a**2==(b**2+c**2):
        print("TRIANGULO RETANGULO")
    if a**2>(b**2+c**2):
        print("TRIANGULO OBTUSANGULO")
    if a**2<(b**2+c**2):
        print("TRIANGULO ACUTANGULO")
    if a==b and b==c:
        print("TRIANGULO EQUILATERO")
    elif a==b or b==c or a==c:
        print("TRIANGULO ISOSCELES")



