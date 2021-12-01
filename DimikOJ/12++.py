for i in range(int(input())):
    k = int(input())
    ans = 0
    while k > 0:
        ans += k//5
        k //= 5
    print(ans)