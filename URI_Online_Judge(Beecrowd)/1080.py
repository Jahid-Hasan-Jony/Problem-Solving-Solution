a=[]
for i in range(1,101):
    a.append(int(input()))
m=max(a)
n=a.index(m)
print(m)
print(n+1)