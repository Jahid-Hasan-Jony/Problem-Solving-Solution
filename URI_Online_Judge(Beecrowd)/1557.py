while True:
    N = int(input())
    if N==0:
        break

    resultado =  []

    n=1
    for i in range(N):
        tmp = []
        for j in range(N):
            if n==0:
                tmp.append(n)
            if n>0:
                tmp.append(n*2)
        resultado.append(tmp)
        n+=1
        if i>1:
            n*2
    for i in range(N):
        tx = ''
        for j in range(N):
            tx += str(resultado[i][j])
        print(tx)
    
