import math
def fact(a):
    a = math.factorial(a)
    a = str(a)
    b = -1
    zero = 0
    for i in range(len(a)):
        if a[b] == "0":
            zero += 1
            b -= 1
        else:
            break
    print(zero)
      
for i in range(int(input())):
    fact(int(input()))
    