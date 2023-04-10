while True:
    num = int(input("Digite um número inteiro positivo menor que 16 para calcular o fatorial (ou digite um número negativo para sair): "))

    if num < 0:
        break
    elif num >= 16:
        print("Número muito grande. Tente novamente.")
        continue

    fat = 1
    for i in range(1, num+1):
        fat *= i

    print(f"O fatorial de {num} é {fat}.")
