# EX 1

# Aplicando for

soma = 0

for i in range(1,6):
  soma = soma + float(input(f"Insira a nota {i}: "))

media = soma / 5

print(f"\nSua média é {media}\n----------\n")



#Aplicando while

soma = 0
numero = 1

while numero < 6:
  nota = float(input(f"Insira sua nota {numero}: "))
  soma = soma + nota
  numero +=1

media = soma / 5
print(f"\nSua média é {media}")