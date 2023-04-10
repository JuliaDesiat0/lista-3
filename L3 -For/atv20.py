n = int(input("Quantas notas serão informadas? "))

soma = 0

for i in range(n):
    nota = float(input("Digite a nota {}: ".format(i+1)))
    soma += nota

media = soma / n

print("A média das notas informadas é: {:.2f}".format(media))
