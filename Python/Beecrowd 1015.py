import math

X1, Y1 =[float(x) for x in input().split()]
X2, Y2 =[float(x) for x in input().split()]

dist = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

print(f"{dist:.4f}")