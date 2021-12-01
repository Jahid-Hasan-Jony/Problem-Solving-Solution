for i in range(int(input())):
    m = ''
    n = int(input())
    for j in range(n+1):
        if j>0:
            if n % j == 0:
                m += str(j) + " " 
    print("Case {}: {}".format(i+1,m[:-1]))
