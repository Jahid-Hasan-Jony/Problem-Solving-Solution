for i in range(int(input())):
    N = int(input(""))
    test = N**(0.5)
    check = round(test)
    print("YES" if test-check==0 else "NO")