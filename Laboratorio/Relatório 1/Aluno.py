class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    # Mostrar presença do aluno
    def presenca(self):
        print(f'O aluno {self.nome} está presente.')