a=float(input())
if a<=400:
    r=(a*15)/100
    e=a+r
    print("Novo salario: %0.2f"%e)
    print("Reajuste ganho: %0.2f"%r)
    print("Em percentual: 15 %")
elif a<=800:
    r=(a*12)/100
    e=a+r
    print("Novo salario: %0.2f"%e)
    print("Reajuste ganho: %0.2f"%r)
    print("Em percentual: 12 %")
elif a<=1200:
    r=(a*10)/100
    e=a+r
    print("Novo salario: %0.2f"%e)
    print("Reajuste ganho: %0.2f"%r)
    print("Em percentual: 10 %")
elif a<=2000:
    r=(a*7)/100
    e=a+r
    print("Novo salario: %0.2f"%e)
    print("Reajuste ganho: %0.2f"%r)
    print("Em percentual: 7 %")
elif a>2000:
    r=(a*4)/100
    e=a+r
    print("Novo salario: %0.2f"%e)
    print("Reajuste ganho: %0.2f"%r)
    print("Em percentual: 15 %")

    