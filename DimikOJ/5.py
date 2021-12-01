t = int(input())
for i in range(t):
    m = int(input())
    for n in range(m):
        print('*'*m)
    if i < t-1:
        print()
    else:
        break
    