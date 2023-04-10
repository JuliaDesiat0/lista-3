num_eleitores = int(input("Digite o número total de eleitores: "))
votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0

for i in range(num_eleitores):
    print("Eleitor {}:".format(i+1))
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    voto = int(input("Digite o número do candidato que você deseja votar: "))
    if voto == 1:
        votos_candidato_1 += 1
    elif voto == 2:
        votos_candidato_2 += 1
    elif voto == 3:
        votos_candidato_3 += 1
    else:
        print("Voto inválido.")

print("Resultado da eleição:")
print("Candidato 1: {} votos".format(votos_candidato_1))
print("Candidato 2: {} votos".format(votos_candidato_2))
print("Candidato 3: {} votos".format(votos_candidato_3))
