a,b,c=[float(x) for x in input().split()]
d,e,f=[float(x) for x in input().split()]

calc1 = b * c
calc2 = e * f
calcFinal = calc1 + calc2

print(f"VALUE TO PAY = R$ {calcFinal:.2f}")