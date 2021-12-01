for i in range(int(input())):
    a,b,c = map(int,input().split())
    r1 = b/((300-c)/6)
    r2 = ((a+1)-b)/(c/6)
    if a < b:
        r2 = 0
    print("{:.2f} {:.2f}".format(r1,r2))