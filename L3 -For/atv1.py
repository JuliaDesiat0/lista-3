limite_superior = int(input("Digite o limite superior do intervalo desejado: "))
incremento = int(input("Digite o incremento desejado: "))
limite_inferior = 10

print("Fahrenheit \t Celsius")
for f in range(limite_inferior, limite_superior + 1, incremento):
    c = round((f - 32) * 5 / 9, 2)
    print("{:.2f}F \t\t {:.2f}C".format(f, c))

