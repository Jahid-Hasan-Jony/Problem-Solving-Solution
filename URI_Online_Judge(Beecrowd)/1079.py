n = int(input())
for i in range(n):
    x,y,z=[float(m) for m in input().split()]
    total=(x*2+y*3+z*5)/10
    print("%0.1F"%total)