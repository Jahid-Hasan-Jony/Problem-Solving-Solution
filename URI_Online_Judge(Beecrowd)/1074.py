m = int(input())

for i in range(m):
    n = int(input())
    if n==0:
        print("NULL")
    else:
        if n>0 and n%2==0:
            print("EVEN POSITIVE")
        elif n<0 and n%2==0:
            print("EVEN NEGATIVE")
        elif n>0 and n%2==1:
            print("ODD POSITIVE")
        elif n<0 and n%2==1:
            print("ODD NEGATIVE")
  
