n=int(input())
m=list(map(int,input().split()))
t=0
th=0
f=0
fi=0
for i in range(n):
    p=m[i]
    if p%2==0:
        t+=1
    if p%3==0:
        th+=1
    if p%4==0:
        f+=1
    if p%5==0:
        fi+=1
print("{} Multiplo(s) de 2".format(t))
print("{} Multiplo(s) de 3".format(th))
print("{} Multiplo(s) de 4".format(f))
print("{} Multiplo(s) de 5".format(fi))