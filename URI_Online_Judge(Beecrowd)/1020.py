N = int(input())
y = N//365
r = N%365
m = r//30
r = r%30
d = r//1

print("{} ano(s)".format(y))
print("{} mes(es)".format(m))
print("{} dia(s)".format(d))
