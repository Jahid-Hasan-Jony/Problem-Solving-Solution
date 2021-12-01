a, b = (float(x) for x in input("").split())
print("%.2f%c" %((b - a)/a*100, '%'))