import math
A,B,C = [float(x) for x in input().split()]
delta = B*B - 4*A*C
if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    x1 = (-B + math.sqrt(delta))/(2*A)
    x2 = (-B - math.sqrt(delta))/(2*A)
    print("R1 = %0.5f"%x1)
    print("R2 = %0.5f"%x2)