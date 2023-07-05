# EX 2

M1 = float(input("Insira sua nota 'M1': "))
M2 = float(input("Insira sua nota 'M2': "))
M3 = float(input("Insira sua nota 'M3': "))

print("\n")

media = (M1 + M2 + M3)/3

if media <= 4:
  print("Você foi REPROVADO(A) :(")
else:
  if media > 6:
    print("Você foi APROVADO(A)!")
  else:
    notaExame = float(input("Você foi condicionado a exame. Se já o realizou, insira a nota obtida: "))
    if notaExame > 6:
      print("Você foi APROVADO(A)!")
    else:
      print("Você foi REPROVADO(A) :(")