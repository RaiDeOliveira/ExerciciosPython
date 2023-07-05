# EX 1

idade = float(input("Digite a sua idade: "))

print("\n")

if 0 <= idade <= 12:
  print("Você é criança.")
else:
  if 13 <= idade <= 17:
    print("Você é adolescente.")
  else:
    if 18 <= idade:
      print("Você é adulto.")
    else:
      print("Idade inválida.")