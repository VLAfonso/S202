from database import Database
from query import TeacherDatabase
from teacher_crud import TeacherCRUD
from teacher_cli import TeacherCLI

# Conectar com banco de dados Neo4j
db = Database("bolt://3.236.187.195:7687", "neo4j", "graph-application-varactor")

# Criar instância da classe TeacherDatabase para interagir com o banco de dados
teacher_db = TeacherDatabase(db)

# Criar instância da classe TeacherCRUD para criar CRUD na entidade Teacher
teacher_crud = TeacherCRUD(db)

# Criar instância da classe TeacherCLI para criar CLI da entidade Teacher
teacher_cli = TeacherCLI(teacher_crud)



# Questão 1
print("Questão 01")
print("a. Busque pelo professor “Teacher” cujo nome seja “Renzo”, retorne o ano_nasc e o CPF.")
renzo = teacher_db.get_teacher_name("Renzo")
print(f"     Ano de Nascimento: {renzo[0][0]}\n     CPF: {renzo[0][1]}")

print("\nb. Busque pelos professores “Teacher” cujo nome comece com a letra “M”, retorne o name e o cpf.")
teachers_m = teacher_db.get_teacher_initial('M')
for teacher in teachers_m:
    print(f"    Nome: {teacher[0]}     CPF: {teacher[1]}")

print("\nc. Busque pelos nomes de todas as cidades “City” e retorne-os.")
cities = teacher_db.get_city()
for city in cities:
    print(f"    {city}")

print("\nd. Busque pelas escolas “School”, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.")
schools = teacher_db.get_school(150, 550)
for school in schools:
    print(f"    Nome: {school[0]}    Endereço: {school[1]}  Número: {school[2]}")
    
# Questão 2
print("\nQuestão 02")
print("a. Encontre o ano de nascimento do professor mais jovem e do professor mais velho.")
teacher_jovem, teacher_velho = teacher_db.get_teacher_age()
print(f"    Mais jovem: {teacher_jovem}    Mais velho: {teacher_velho}")

print("\nb. Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade “population”.")
avg_population = teacher_db.get_avg_population()
print(f"    {avg_population:.2f}")

print("\nc. Encontre a cidade cujo CEP seja igual a “37540-000” e retorne o nome com todas as letras “a” substituídas por “A”.")
city = teacher_db.get_city_cep("37540-000")
print(f"    {city}")

print("\nd. Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.")
teachers_char = teacher_db.get_teacher_char()
for teacher in teachers_char:
    print(f"    {teacher[0]}")

# Questão 03
print("\nQuestão 03")
print("b. Utilizando a classe TeacherCRUD() crie um Teacher com as seguintes características:\nname: 'Chris Lima',\nano_nasc:1956,\ncpf: '189.052.396-66'")
teacher_crud.create('Chris Lima', 1956, '189.052.396-66')

print("\nc. Utilizando a classe TeacherCRUD() pesquise o professor com o name de \"Chris Lima\" .")
chris = teacher_crud.read("Chris Lima")
print(f"    Ano de Nascimento: {chris[0][0]}    CPF: {chris[0][1]}")

print("\nd. Utilizando a classe TeacherCRUD() altere o cpf do “Teacher” de name \"Chris Lima\" para \"162.052.777-77\" .")
teacher_crud.update("Chris Lima", "162.052.777-77")
# Mostrar alteração
chris = teacher_crud.read("Chris Lima")
print(f"    Ano de Nascimento: {chris[0][0]}    CPF: {chris[0][1]}")

print("\ne. Crie um CLI utilizando orientação a objetos como visto em aula.\n")
teacher_cli.run()

# Fechar conexão com o banco de dados
db.close()