num = int(input("Digite um número inteiro: "))

if num <= 1:
    print("Não é um número primo.")
else:
    primo = True
    divisores = []
    for i in range(2, num):
        if num % i == 0:
            primo = False
            divisores.append(i)

    if primo:
        print("É um número primo.")
    else:
        print("Não é um número primo. É divisível por:", divisores)
