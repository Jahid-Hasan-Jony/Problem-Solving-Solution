a,b,c,d=[int(m) for m in input().split()]
p=a*60+b
q=c*60+d
r=q-p
h=r//60
i=r%60
if a==c and b==d:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif a<c:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h,i))
elif a>c:
    if c<=12 and b>d:
        h=23-(a-c)
        i=60-(b-d)
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h,i))
    elif c<=12 and b<d:
        h=24-(a-c)
        i=d-b
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h,i))
elif a==c:
    if b>d:
        h=23
        i=60-(b-d)
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h,i))
    elif b<d:
        h=0
        i=(d-b)
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h,i))
        
        
        
   