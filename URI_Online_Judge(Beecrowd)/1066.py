even=0
odd=0
pos=0
neg=0
for i in range(5):
    n = int(input())
    if n%2==0:
        even+=1
    else:
        odd+=1
    if n>0:
        pos+=1
    if n<0:
        neg+=1
print("{} valor(es) par(es)".format(even))
print("{} valor(es) impar(es)".format(odd))
print("{} valor(es) positivo(s)".format(pos))
print("{} valor(es) negativo(s)".format(neg))
        