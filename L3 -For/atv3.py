pares = 0
impares = 0

for i in range(6):
    valor = int(input(f"Digite o {i+1}º valor: "))
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"{pares} valores pares e {impares} valores ímpares")
