for i in range(int(input())):
    n = list(map(int,input().split()))
    n.sort()
    m = ''
    
    for j in range(len(n)):
        m += str(n[j]) + ' '
        
    print("Case {}: {}".format(i+1,m[:-1]))