# Importação das classes
from Professor import Professor
from Aluno import Aluno
from Aula import Aula

# Execução de um exemplo de uso
professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_presenca()
