a = int(input("Informe o 1o. valor: "))
b = int(input("Informe o 2o. valor: "))
c = int(input("Informe o 3o. valor: "))

if (a > b):
    a, b = b, a
if (a > c):
    a, c = c, a
if (b > c):
    b, c = c, b

print(f"\n1o. valor: {a}")
print(f"2o. valor: {b}")
print(f"3o. valor: {c}")
