# EX 2

boletim = {}
soma = 0

# Armazena o nome e a nota de cada aluno dentro do dicionário "boletim" como key e value, respectivamente
for i in range(1,4):
  nome = input(f"Digite o NOME do(a) aluno(a) {i}: ")
  nota = float(input(f"Digite a NOTA do(a) aluno(a) {i}: "))
  boletim[nome] = nota

print("\n", boletim, "\n\n")


# Soma todos os valores (notas) das keys (nomes dos alunos) do dicionário "boletim"
for valorNota in boletim.values():
  soma = soma + valorNota

# Obtém a média da turma dividindo a soma das notas pela quantidade de alunos
media = soma / len(boletim.keys())



print(f"A média da turma é {round(media, 2)}")