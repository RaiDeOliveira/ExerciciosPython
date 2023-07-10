# EX 1

soma = 0
lista = []

for _ in range(1,6):
  lista.append(int(input("Digite um número: ")))

for n in lista:
  soma = soma + n

print(soma)