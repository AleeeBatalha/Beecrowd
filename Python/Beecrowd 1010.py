A, B, C=[float(x) for x in input().split()]
D, E, F=[float(x) for x in input().split()]

calc1 = B * C
calc2 = E * F
calcFinal = calc1 + calc2

print(f"VALOR A PAGAR: R$ {calcFinal:.2f}")