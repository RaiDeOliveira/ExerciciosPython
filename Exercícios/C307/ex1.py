# EX 1


alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open("Exercícios/C307/boletim.txt", 'w') as boletim:
    for aluno, nota in alunos.items():
        boletim.write(f'{aluno},{nota}\n')
    boletim.close()

with open("Exercícios/C307/boletim.txt") as boletim:
    notas = boletim.readlines()
    for linhas in notas:
        print(linhas)
    boletim.close()