numero = int(input("Digite um número entre 0 e 1000: "))

while numero < 0 or numero > 1000:
    print("Número inválido. Tente novamente.")
    numero = int(input("Digite um número entre 0 e 1000: "))

print("Número válido.")
