V = int(input())

print(V)

print(f"{V//100} nota(s) de R$ 100,00")
V %= 100
print(f"{V//50} nota(s) de R$ 50,00")
V %= 50
print(f"{V//20} nota(s) de R$ 20,00")
V %= 20
print(f"{V//10} nota(s) de R$ 10,00")
V %= 10
print(f"{V//5} nota(s) de R$ 5,00")
V %= 5
print(f"{V//2} nota(s) de R$ 2,00")
V %= 2
print(f"{V} nota(s) de R$ 1,00")