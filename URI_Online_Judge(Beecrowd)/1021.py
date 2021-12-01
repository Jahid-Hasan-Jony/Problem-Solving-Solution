m = float (input())
nota = [100,50,20,10,5,2]
moedas = [1,.50,.25,.10,.05,.01]
print("NOTAS:")
for notas in nota:
    n=int(m/notas)
    print ("{} nota(s) de R$ {:.2f}".format(n,notas))
    m-=n*notas
print("MOEDAS:")
for moeda in moedas:
    n=int(round(m,2)/moeda)
    print ("{} moeda(s) de R$ {:.2f}".format(n,moeda))
    m-=n*moeda
    
    

   
  
    

