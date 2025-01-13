A, B, C = [int(x) for x in input().split()]

farinha = 2
ovos = 3
leite = 5

bolofarinha = A // farinha
boloovos = B // ovos
bololeite = C // leite

maxbolos = min(bolofarinha, boloovos, bololeite)

print(f"{maxbolos}")
