a=int(input())
c=0
r=0
s=0
for i in range(a):
    n=input().split()
    m=n[0]
    m=int(m)
    p=n[-1]
    if p=="C":
        c=c+m
    if p=="R":
        r=r+m
    if p=="S":
        s=s+m
t=c+r+s
print("Total: {} cobaias".format(t))
print("Total de coelhos: {}".format(c))
print("Total de ratos: {}".format(r))
print("Total de sapos: {}".format(s))
print("Percentual de coelhos: {} %".format("%0.2f"%((c/t)*100)))
print("Percentual de ratos: {} %".format("%0.2f"%((r/t)*100)))
print("Percentual de sapos: {} %".format("%0.2f"%((s/t)*100)))