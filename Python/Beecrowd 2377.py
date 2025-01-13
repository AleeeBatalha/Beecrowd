L, D = [int(X) for X in input().split()]
K, P = [int(X) for X in input().split()]

custo_quilometro = L * K

numero_pedagios = L // D

custo_pedagios = numero_pedagios * P

custo_total = custo_quilometro + custo_pedagios

print(custo_total)
