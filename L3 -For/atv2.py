# leitura das dimensões da matriz
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

# construção e impressão da matriz
for i in range(linhas):
  for j in range(colunas):
    print(f"A{i},{j}", end="")
    if j == colunas-1:
      print("#", end="")
    else:
      print(" ", end="")
  print()

