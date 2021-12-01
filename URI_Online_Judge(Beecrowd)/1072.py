x=int(input())
on=0
out=0
for i in range(x):
    n=int(input())
    if n>=10 and n<=20:
        on+=1
    else:
        out+=1
print("{} in".format(on))
print("{} out".format(out))
        