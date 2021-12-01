while True:
    try:
        n = int(input())
        n += 1
        m = []
        for i in range(n):
            if i<2:
                m.append(i)
        
            else:
                for j in range(i):
                    m.append(i)
        txt = ''
        for i in range(len(m)):
            txt += str(m[i]) + " "
        print("Caso {}: {} numero".format(m[-1]+1,len(m)))
        print(txt[:-1])
        print()
    except EOFError:
        break