S = input()
C = 0
A = 0
for i in range(12):
    for j in range(12):
        N = float(input())
        if(i + j >= 12 and j - i >= 1):
            C+=N
            A+=1

if(S == 'S'):
     print("%.1f" %C)
else:
     print("%.1f" %(C/A))