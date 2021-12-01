S = input()
n=12
C = 0
A = 0
for i in range(12):
    for j in range(12):
        N = float(input())
        if i>0 and j>0 and j>=n:
            C+=N
            A+=1
    n-=1        
if(S == 'S'):
     print("%.1f" %C)
else:
     print("%.1f" %(C/A))