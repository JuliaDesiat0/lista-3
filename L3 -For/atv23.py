quantidadeturmas = int(input("Digite a quantidade de turmas: "))
totalalunos = 0

for i in range(1, quantidadeturmas+1):
    while True:
        quantidade_alunos = int(input(f"Digite a quantidade de alunos da turma {i}: "))
        if quantidade_alunos <= 40:
            break
        print("Turma não pode ter mais de 40 alunos. Digite novamente.")
        
    totalalunos += quantidade_alunos

media_alunos = totalalunos / quantidadeturmas

print(f"A média de alunos por turma é {media_alunos:.2f}.")
