class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    # Adicionar aluno à aula
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    # Listar informação sobre aula e os alunos presentes
    def listar_presenca(self):
        print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')
        for aluno in self.alunos:
            aluno.presenca()

