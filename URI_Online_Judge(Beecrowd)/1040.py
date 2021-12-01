N1, N2, N3, N4 = [float(x) for x in input().split()]
N1 = N1*2
N2 = N2*3
N3 = N3*4
N4 = N4*1
av = (N1+N2+N3+N4)/10

print("Media: %0.1f"%av)

if av>=7:
    print("Aluno aprovado.")
elif av<5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: %0.1f"%e)
    av2 = (e+av)/2
    if av2>=5.0:
        print("Aluno aprovado.")
        print("Media final: %0.1f"%av2)
    else:
        print("Aluno reprovado.")
        
        
        
#elif av>=5.0 and av<=6.9:
    #print("Aluno em exame.")  


