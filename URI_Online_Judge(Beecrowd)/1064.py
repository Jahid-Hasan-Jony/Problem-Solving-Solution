m=0
j=0
for i in range(6):
    n = float(input())
    if n>0:
        m+=n
        j+=1
avg = m/j
print("{} valores positivos".format(j))
print("%0.1f"%avg)
    