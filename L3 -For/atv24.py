quantidadecds = int(input("Digite a quantidade de CDs da coleção: "))
totalgasto = 0

for i in range(1, quantidadecds+1):
    preco_cd = float(input(f"Digite o valor gasto no CD {i}: R$ "))
    totalgasto += preco_cd

media_gasto = totalgasto / quantidadecds

print(f"O valor total investido na coleção de CDs é R$ {totalgasto:.2f}.")
print(f"A média de gastos por CD é R$ {media_gasto:.2f}.")
