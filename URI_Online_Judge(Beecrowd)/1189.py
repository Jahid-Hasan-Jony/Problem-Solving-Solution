S = input()
C = 0
A = 0
for i in range(12):
    for j in range(12):
        N = float(input())
        if(i - j >= 1 and i + j <= 10):
            C+=N
            A+=1

if(S == 'S'):
     print("%.1f" %C)
else:
     print("%.1f" %(C/A))