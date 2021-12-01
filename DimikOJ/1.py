def gcd(a,b):
    while b > 0:
        a, b = b, a % b
        print(a)
        print(b)
    return print(a)
gcd(20,25)