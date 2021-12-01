def salary():
    print("Novo salario: %0.2f"%e)
    print("Reajuste ganho: %0.2f"%r)
    print("Em percentual: {} %".format(p))
a=float(input())
if a<=400:
    r=(a*15)/100
    e=a+r
    p=15
    salary()
elif a<=800:
    r=(a*12)/100
    e=a+r
    p=12
    salary()
elif a<=1200:
    r=(a*10)/100
    e=a+r
    p=10
    salary()
elif a<=2000:
    r=(a*7)/100
    e=a+r
    p=7
    salary()
elif a>2000:
    r=(a*4)/100
    e=a+r
    p=4
    salary()

    
