a = int(input())
b = list(map(int,input().split()))
count=0
for i in range(len(b)):
    if b[i]==a:
        count+=1
    
print(count)
        