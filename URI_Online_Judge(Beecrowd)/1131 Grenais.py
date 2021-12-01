w=0
yw=0
d=0
m=0
while 1:
    x,y=[int(m) for m in input().split()]
    print("Novo grenal (1-sim 2-nao)")
    m+=1
    if x>y:
        w+=1
    elif x<y:
        yw+=1
    else:
        d+=1
    z=int(input())
    if z==1:
        continue
    else:
        break
print("{} grenais".format(m))
print("Inter:{}".format(w))
print("Gremio:{}".format(yw))
print("Empates:{}".format(d))
if w>yw:
    print("Inter venceu mais")
elif w<yw:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")
    
