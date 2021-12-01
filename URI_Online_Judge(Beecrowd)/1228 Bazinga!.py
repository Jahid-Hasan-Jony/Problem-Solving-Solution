t=int(input())
for i in range(t):
    i+=1
    n=input().split()
    if n[0] == n[1]:
        print("Caso #{}: De novo!".format(i))
    elif n[0]=="tesoura" and n[1]=="papel":
        print("Caso #{}: Bazinga!".format(i))
    elif n[0]=="papel" and n[1]=="pedra":
        print("Caso #{}: Bazinga!".format(i))
    elif n[0]=="pedra" and n[1]=="lagarto":
        print("Caso #{}: Bazinga!".format(i))
    elif n[0]=="lagarto" and n[1]=="Spock":
        print("Caso #{}: Bazinga!".format(i))
    elif n[0]=="Spock" and n[1]=="tesoura":
        print("Caso #{}: Bazinga!".format(i))
    elif n[0]=="tesoura" and n[1]=="lagarto":
        print("Caso #{}: Bazinga!".format(i))
    elif n[0]=="lagarto" and n[1]=="papel":
        print("Caso #{}: Bazinga!".format(i))
    elif n[0]=="papel" and n[1]=="Spock":
        print("Caso #{}: Bazinga!".format(i))
    elif n[0]=="Spock" and n[1]=="pedra":
        print("Caso #{}: Bazinga!".format(i))
    elif n[0]=="pedra" and n[1]=="tesoura":
        print("Caso #{}: Bazinga!".format(i))
    else:
        print("Caso #{}: Raj trapaceou!".format(i))
        
    
    
    