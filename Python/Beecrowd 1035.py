A, B, C, D =[float(x) for x in input().split()]

if((B > C) and (D > A)) and (C + D > A + B) and (A % 2):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
