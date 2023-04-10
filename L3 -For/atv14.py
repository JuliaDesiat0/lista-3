N = int(input("Digite a quantidade de números: "))

# inicializa as variáveis com o primeiro número lido
maior = menor = soma = int(input("Digite um número: "))

# loop para ler os próximos números e atualizar as variáveis
for i in range(1, N):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num

# imprime os resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A soma dos números é: {soma}")
