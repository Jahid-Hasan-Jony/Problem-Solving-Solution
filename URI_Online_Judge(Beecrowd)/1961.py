a,b = map(int,input().split())
c = input().split()
lista=[]
lista.append(c)
n=0
m=1
for i in range(b-1):
    if (int(lista[0][m]) - int(lista[0][n]) <= a):
        n+=1
        m+=1
        
    else:
        print("GAME OVER")
        break
if n==b-1:
    print("YOU WIN")
    