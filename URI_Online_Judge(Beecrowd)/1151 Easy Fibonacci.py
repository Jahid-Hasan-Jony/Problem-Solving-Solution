n=int(input())
f=[0,1,1]
s=''
for i in range(n):
    if i>=3:
        a=f[-1]+f[-2]
        f.append(a)

for i in range(n):
    s+=str(f[i])+" "
print(s[:-1])