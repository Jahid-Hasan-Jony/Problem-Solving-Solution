A,B,C=map(float,input().split())
pi = 3.14159
tringle = 0.5*A*C
circle = pi*C*C
trapizium = (A + B)/2*C
squer = B*B
rectangle = A*B
print("TRIANGULO: %.3f"%tringle)
print("CIRCULO: %.3f"%circle)
print("TRAPEZIO: %.3f"%trapizium)
print("QUADRADO: %.3f"%squer)
print("RETANGULO: %.3f"%rectangle)