while True:
    user=int(input())
    if user==0:
        break
    list1=[]
    m=0
    for i in range(user):
        list2=[]
        n=2
        for j in range(user):
            if i==0 and j==0:
                list2.append(i+1)
            if i==0 and j==1:
                list2.append(n)
            if i==0 and j>1:
                list2.append(n*2)
                n*=2
            if i>0 and j==0:
                n-=n
                n+=list1[m][1]
                list2.append(n)
                m+=1
            if i>0 and j>0:
                n*=2
                list2.append(n)
        list1.append(list2)
    for i in range(user):
        tx = ''
        for j in range(user):
            if user==1:
                tx += "%d" %list1[i][j]
            elif user==2:
                if j==0:
                    tx += "%d" %list1[i][j]
                else:
                    tx += " %d" %list1[i][j]
            elif user==3 or user==4:
                if j==0:
                    tx += " %d" %list1[i][j]
                else:
                    tx += "%3d" %list1[i][j]
            elif user==5:
                if j==0:
                    tx += "%3d" %list1[i][j]
                else:
                    tx += "%4d" %list1[i][j]
            elif user==6 or user==7:
                if j==0:
                    tx += "%4d" %list1[i][j]
                else:
                    tx += "%5d" %list1[i][j]
            elif user==8 or user==9:
                if j==0:
                    tx += "%5d" %list1[i][j]
                else:
                    tx += "%6d" %list1[i][j]
            elif user==10:
                if j==0:
                    tx += "%6d" %list1[i][j]
                else:
                    tx += "%7d" %list1[i][j]
            elif user==11 or user==12:
                if j==0:
                    tx += "%7d" %list1[i][j]
                else:
                    tx += "%8d" %list1[i][j]
            elif user==13 or user==14:
                if j==0:
                    tx += "%8d" %list1[i][j]
                else:
                    tx += "%9d" %list1[i][j]
            elif user==15:
                if j==0:
                    tx += "%9d" %list1[i][j]
                else:
                    tx += "%10d" %list1[i][j]
        print(tx[0:])
    print("")
