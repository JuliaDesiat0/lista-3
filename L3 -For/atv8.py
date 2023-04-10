capacidade_maxima = int(input("Digite a capacidade máxima do restaurante: "))
clientes = 0

while clientes < capacidade_maxima:
    clientes += int(input("Digite a quantidade de clientes que chegaram: "))

print("Restaurante lotado, não há mais mesas disponíveis.")
