def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return print(int(a * b / gcd(a, b)))

for i in range(int(input())):
    a,b = map(int,input().split())
    lcm(a,b)