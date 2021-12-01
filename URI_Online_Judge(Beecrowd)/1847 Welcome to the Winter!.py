a,b,c=map(int,input().split())
if a>b<=c:
    print(":)")
elif a<b<c and b-a < c-b:
    print(":)")
elif a>b and b-c==a-b:
    print(":)")
elif a>b and c>b:
    print(":)")
elif a==b and b<c:
    print(":)")
else:
    print(":(")
    