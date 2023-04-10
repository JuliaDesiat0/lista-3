while True:
    nome = input("Digite o seu nome: ")
    if len(nome) > 3:
        break
    print("Nome inválido. Deve ter mais que 3 caracteres.")

while True:
    idade = int(input("Digite a sua idade: "))
    if 0 <= idade <= 150:
        break
    print("Idade inválida. Deve estar entre 0 e 150.")

while True:
    salario = float(input("Digite o seu salário: "))
    if salario > 0:
        break
    print("Salário inválido. Deve ser maior que zero.")

while True:
    sexo = input("Digite o seu sexo: ").lower()
    if sexo == "f" or sexo == "m":
        break
    print("Sexo inválido. Deve ser 'f' ou 'm'")

while True:
    estado_civil = input("Digite o seu estado civil (s/c/v/d): ").lower()
    if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
        break
    print("Estado civil inválido. Deve ser 's', 'c', 'v' ou 'd'.")

print("Informações válidas.")
