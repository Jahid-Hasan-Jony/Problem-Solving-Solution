import math
for i in range(int(input())):
    Sentence=input().split()
    word=set(Sentence)
    N=math.factorial(len(Sentence))
    M=1
    for r in word:
        sum=0
        for o in Sentence:
            if(r==o):
                sum+=1
        if(sum>1):
            M*=math.factorial(sum)
    print("1/",end="")
    print(N//M)