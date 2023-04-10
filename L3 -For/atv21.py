n = int(input("Digite o número de pessoas: "))
idades = []

for i in range(n):
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    idades.append(idade)

media = sum(idades) / n

if media <= 25:
    print("A média de idade da turma é de {:.1f} anos. A turma é considerada JOVEM.".format(media))
elif media <= 60:
    print("A média de idade da turma é de {:.1f} anos. A turma é considerada ADULTA.".format(media))
else:
    print("A média de idade da turma é de {:.1f} anos. A turma é considerada IDOSA.".format(media))

