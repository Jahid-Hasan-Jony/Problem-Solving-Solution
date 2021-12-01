S = input()
n=10
m=0
C = 0
A = 0
for i in range(12):
    for j in range(12):
        N = float(input())
        if i<5 and j>m and j<=n:
            C+=N
            A+=1
    n-=1
    m+=1
if(S == 'S'):
     print("%.1f" %C)
else:
     print("%.1f" %(C/A))