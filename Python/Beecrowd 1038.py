cod, qut =[int(x) for x in input().split()]
prcs = [4.00, 4.50, 5.00, 2.00, 1.50]

total =  qut * prcs[cod - 1]

print(f"Total: R${total:.2f}")
