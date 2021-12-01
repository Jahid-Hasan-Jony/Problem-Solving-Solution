a,b,c= [float(x) for x in input().split()]
area = ((a+b)*c)/2
Perimetro = a+b+c

if (a+b>c and a+c>b and b+c>a):
    print("Perimetro = %0.1f"%Perimetro)
    
else:
    print("Area = %0.1f"%area)