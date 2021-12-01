N = int(input())
S = input()   
C = 0

for i in range(12):
    for j in range(12):
        N2 = float(input())
        if(i == N):
            C += N2
               
if(S == 'S'):
     print("%.1f" %C)
else:
     print("%.1f" %(C/12.0))