x, y = [float(x) for x in input().split()]
if x==0:
    if y==0:
        print("Origem")
    else:
        print("Eixo Y")
        
elif x>0.0 and y>0.0:
    print("Q1")
elif x<0.0 and y>0.0:
    print("Q2")
elif x<0.0 and y<0.0:
    print("Q3")
elif x>0.0 and y<0.0:
    print("Q4")
else:
    print("Eixo X")


