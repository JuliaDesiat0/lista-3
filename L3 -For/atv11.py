n = int(input("Digite o número de termos que deseja gerar: "))
fibonacci = [1, 1]

if n == 1:
  print(fibonacci[0])
elif n == 2:
  print(fibonacci)
else:
  for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
  print(fibonacci)
