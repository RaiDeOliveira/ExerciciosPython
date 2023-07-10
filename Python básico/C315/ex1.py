# EX 1

class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    # EX 2

    def calculaMedia(self):
        return (self.nota1 + self.nota2) / 2
    
    def mostraDados(self):
        return (f"Nome: {self.nome}\nNota 1: {self.nota1}\nNota 2: {self.nota2}")
    
    def resultado(self):
        media = (self.nota1 + self.nota2) / 2
        if media < 6:
            return "Aluno(a) não aprovado(a).\n"
        else:
            return "Aluno(a) aprovado(a).\n"

# EX 3 

aluno1 = aluno('Ana', 10, 9)
aluno2 = aluno('Carlos', 1, 10)

print(aluno1.mostraDados())
print(f"Média: {aluno1.calculaMedia()}")
print(aluno1.resultado())

print(aluno2.mostraDados())
print(f"Média: {aluno2.calculaMedia()}")
print(aluno2.resultado())