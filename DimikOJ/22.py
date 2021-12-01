import sympy
for i in range(int(input())):
    a,b = map(int,input().split())  
    m = 0
    l = []
    for n in range(1,100001):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    break  
            else:
                l.append(n)
    print(l.index(b))  
            