while True:
    try:
        t=int(input())
        n=list(map(int,input().split()))
        m=max(n[:t])
        if m<10:
            print(1)
        if m>=10 and m<20:
            print(2)
        if m>=20:
            print(3)
    except EOFError:
        break
