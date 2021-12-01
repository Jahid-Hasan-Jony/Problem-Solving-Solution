for i in range(int(input())):
    n = input()
    vowel = 'AaEeIiOoUu'
    v,c = '',''
    for x in n:
        if (x>="A"and x<="Z") or (x>="a" and x<="z"):
            if x in vowel:
                v += x
            else:
                c += x
    print(v)
    print(c)
    
        
    
    