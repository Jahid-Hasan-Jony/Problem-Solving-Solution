x,y=[int(n) for n in input().split()]
count=0
if 1<x<20 and x<y<100000:
    for i in range(1,y+1):
        print("{} ".format(i),end="")
        count+=1
        if (count%x==0):
            print(" ")
    
            
         
                
        
        
